import re
from ..symbol_table import Type

class CodeGenerator:
    def __init__(self, ir):
        self.ir = ir
        self.action_index = {
            name: i for i, name in enumerate(ir.actions)
        }

    def generate(self):
        lines = []
        lines += [
            "import numpy as np",
            "from gymnasium import spaces, Env",
            "",
            "class GeneratedEnv(Env):",
            "    def __init__(self):",
            "        self.observation_space = spaces.Dict({"
        ]

        for state in self.ir.states.values():
            if state.type_enum == Type.CONTINUOUS:
                try:
                    low = float(eval(state.domain[0]))
                    high = float(eval(state.domain[1]))
                except:
                    low = 0.0
                    high = 1.0
                lines.append(
                    f"            '{state.name}': spaces.Box({low}, {high}, (1,), np.float32),"
                )
            elif state.type_enum == Type.DISCRETE:
                n = len(state.domain)
                lines.append(
                    f"            '{state.name}': spaces.Discrete({n}),"
                )

        lines += [
            "        })",
            f"        self.action_space = spaces.Discrete({len(self.ir.actions)})",
            "        self.reset()",
            "",
            "    def reset(self, seed=None, options=None):",
            "        super().reset(seed=seed)"
        ]

        # Initialize states
        for state in self.ir.states.values():
            if state.type_enum == Type.CONTINUOUS:
                 try:
                     low_val = float(eval(state.domain[0]))
                     high_val = float(eval(state.domain[1]))
                 except:
                     low_val = 0.0
                     high_val = 1.0
                 
                 # Safe Initialization: Center 20%
                 span = high_val - low_val
                 init_low = low_val + (span * 0.4)
                 init_high = low_val + (span * 0.6)
                 lines.append(f"        self.{state.name} = np.random.uniform({init_low}, {init_high})")
            else:
                 lines.append(f"        self.{state.name} = 0")

        lines += [
            "        return self._get_obs(), {}",
            "",
            "    def step(self, action):"
        ]

        # ALWAYS
        for rule in self.ir.always_rules:
            self._generate_block(rule.statements, lines, "        ")


        # WHEN → if/elif
        if self.ir.when_rules:
            first = True
            for rule in self.ir.when_rules:
                for act in rule.actions:
                    idx = self.action_index[act]
                    keyword = "if" if first else "elif"
                    lines.append(f"        {keyword} action == {idx}:")
                    first = False
                    
                    for a in rule.assignments:
                        lines.append(
                            f"            self.{a.target} = {self._expr(a.expr)}"
                        )
            lines += [
                "        else:",
                "            pass"
            ]
        
        # REWARDS
        lines.append("")
        lines.append("        reward = 0.0")
        for r in self.ir.rewards:
             cond = self._expr(r.condition)
             val = self._expr(r.reward_expr)
             lines.append(f"        if {cond}:")
             lines.append(f"            reward += {val}")

        lines += [
            "",
            "        if hasattr(self, 'done'):",
            "            done = bool(self.done)",
            "        else:",
            "            done = False",
            "        return self._get_obs(), reward, done, False, {}",
            "",
            "    def _get_obs(self):",
            "        return {"
        ]

        for name, state in self.ir.states.items():
            if state.type_enum == Type.CONTINUOUS:
                lines.append(f"            '{name}': np.array([self.{name}], dtype=np.float32),")
            else:
                lines.append(f"            '{name}': self.{name},")
        lines += [
            "        }",
            "",
            "    def render(self):",
            "        print('-' * 20)",
            "        print(f'Step State:')"
        ]
        
        for name in self.ir.states:
             lines.append(f"        print(f'{name}: {{self.{name}}}')")
             
        lines += [
             "        print('-' * 20)"
        ]

        return "\n".join(lines)

    def generate_training_script(self, env_filename="generated_env.py"):
        # Default config
        algo = self.ir.training_config.get("Algo", "PPO")
        timesteps = self.ir.training_config.get("Timesteps", "10000")
        
        lines = [
            f"from {env_filename.replace('.py', '')} import GeneratedEnv",
            f"from stable_baselines3 import {algo}",
            "",
            "env = GeneratedEnv()",
            f"model = {algo}('MultiInputPolicy', env, verbose=1)",
            f"model.learn(total_timesteps={timesteps})",
            "",
            "print('Training finished!')",
            "model.save('rl_model')",
            "obs, _ = env.reset()",
            "# Test run",
            "for i in range(10):",
            "    action, _states = model.predict(obs, deterministic=True)",
            "    obs, reward, done, truncated, info = env.step(action)",
            "    print(f'Step {i}: reward={reward}')"
        ]
        return "\n".join(lines)

    def generate_eval_script(self, env_filename="generated_env.py"):
         algo = self.ir.training_config.get("Algo", "PPO")
         lines = [
            f"from {env_filename.replace('.py', '')} import GeneratedEnv",
            f"from stable_baselines3 import {algo}",
            "import time",
            "",
            "env = GeneratedEnv()",
            f"model = {algo}.load('rl_model', env=env)",
            "",
            "print('Starting Evaluation Loop...')",
            "obs, _ = env.reset()",
            "# Override state for showcase",
            "if hasattr(env, 'x'): env.x = 2.0",
            "if hasattr(env, 'y'): env.y = 10.0",
            "if hasattr(env, 'vx'): env.vx = 0.0",
            "if hasattr(env, 'vy'): env.vy = 0.0",
            "if hasattr(env, 'landed'): env.landed = 0",
            "if hasattr(env, 'crashed'): env.crashed = 0",
            "if hasattr(env, 'done'): env.done = 0",
            "obs = env._get_obs()",
            "env.render()",
            "",
            "for i in range(20):",
            "    action, _states = model.predict(obs, deterministic=True)",
            "    print(f'\\n--- Step {i+1} ---')",
            "    print(f'Action: {action}')",
            "    obs, reward, done, truncated, info = env.step(action)",
            "    env.render()",
            "    print(f'Reward: {reward}')",
            "    time.sleep(0.5)",
            "    if done:",
            "        print('Episode Finished')",
            "        obs, _ = env.reset()",
         ]
         return "\n".join(lines)

    def _generate_block(self, statements, lines, indent):
        from ..ir import AssignmentIR, IfRuleIR
        for stmt in statements:
             if isinstance(stmt, AssignmentIR):
                 lines.append(f"{indent}self.{stmt.target} = {self._expr(stmt.expr)}")
             elif isinstance(stmt, IfRuleIR):
                 cond = self._expr(stmt.condition)
                 lines.append(f"{indent}if {cond}:")
                 self._generate_block(stmt.statements, lines, indent + "    ")

    def _expr(self, expr):
        # Improved replacement using regex to match whole words only
        # This prevents 'x' matching inside 'max_x'
        for s in self.ir.states:
            # Match word boundary, variable name, word boundary
            pattern = r'\b' + re.escape(s) + r'\b'
            expr = re.sub(pattern, f"self.{s}", expr)
        return expr
