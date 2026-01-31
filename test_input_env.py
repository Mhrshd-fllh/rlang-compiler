import numpy as np
from gymnasium import spaces, Env

class GeneratedEnv(Env):
    def __init__(self):
        self.observation_space = spaces.Dict({
            'pos_y': spaces.Box(0.0, 100.0, (1,), np.float32),
            'battery': spaces.Box(0.0, 100.0, (1,), np.float32),
            'charge': spaces.Box(0.0, 100.0, (1,), np.float32),
            'score': spaces.Box(0.0, 100.0, (1,), np.float32),
            'mode': spaces.Discrete(2),
        })
        self.action_space = spaces.Discrete(2)
        self.reset()

    def reset(self):
        self.pos_y = 0
        self.battery = 0
        self.charge = 0
        self.score = 0
        self.mode = 0
        return self._get_obs()

    def step(self, action):
        self.battery = self.battery-0.1
        self.charge = self.charge*0.9
        match action:
            case 0:
                self.pos_x = self.pos_y+1
            case _:
                pass

        reward = 0
        done = False
        return self._get_obs(), reward, done, False, {}

    def _get_obs(self):
        return {
            'pos_y': self.pos_y,
            'battery': self.battery,
            'charge': self.charge,
            'score': self.score,
            'mode': self.mode,
        }