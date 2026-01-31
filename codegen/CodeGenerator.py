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

        for name, t in self.ir.states.items():
            if t.name == "CONTINUOUS":
                lines.append(
                    f"            '{name}': spaces.Box(0.0, 100.0, (1,), np.float32),"
                )
            else:
                lines.append(
                    f"            '{name}': spaces.Discrete(2),"
                )

        lines += [
            "        })",
            f"        self.action_space = spaces.Discrete({len(self.ir.actions)})",
            "        self.reset()",
            "",
            "    def reset(self):"
        ]

        for name in self.ir.states:
            lines.append(f"        self.{name} = 0")

        lines += [
            "        return self._get_obs()",
            "",
            "    def step(self, action):"
        ]

        # ALWAYS
        for rule in self.ir.always_rules:
            for a in rule.assignments:
                lines.append(f"        self.{a.target} = {self._expr(a.expr)}")

        # WHEN → match
        lines.append("        match action:")
        for rule in self.ir.when_rules:
            for act in rule.actions:
                idx = self.action_index[act]
                lines.append(f"            case {idx}:")
                for a in rule.assignments:
                    lines.append(
                        f"                self.{a.target} = {self._expr(a.expr)}"
                    )

        lines += [
            "            case _:",
            "                pass",
            "",
            "        reward = 0",
            "        done = False",
            "        return self._get_obs(), reward, done, False, {}",
            "",
            "    def _get_obs(self):",
            "        return {"
        ]

        for name in self.ir.states:
            lines.append(f"            '{name}': self.{name},")

        lines += [
            "        }"
        ]

        return "\n".join(lines)

    def _expr(self, expr):
        for s in self.ir.states:
            expr = expr.replace(s, f"self.{s}")
        return expr
