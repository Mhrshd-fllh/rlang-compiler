# RLang Grammar Specification

This document provides a detailed reference for the RLang syntax. RLang files (`.rlang`) describe Reinforcement Learning environments using a structured, readable format.

## 1. Environment Wrapper

Every RLang file must define exactly one environment block.

```rlang
ENVIRONMENT MyEnvName {
    // Definitions go here...
}
```

## 2. State Definition (`STATE`)

Defines the observation space. Supports continuous and discrete variables.

```rlang
STATE {
    // Continuous variable: name: continuous(min, max);
    pos_x: continuous(0.0, 10.0);
    velocity: continuous(-5.0, 5.0);

    // Discrete variable: name: discrete[Label1, Label2, ...];
    status: discrete[Idle, Walking, Running];
    
    // Flags (useful for internal logic):
    crashed: discrete[No, Yes];
}
```

## 3. Action Definition (`ACTIONS`)

Defines the discrete action space.

```rlang
ACTIONS {
    wait,   // Action 0
    left,   // Action 1
    right,  // Action 2
    jump    // Action 3
}
```

## 4. Dynamics (`DYNAMICS`)

Defines how the state changes in response to actions and time.

### `always` Block
Logic inside `always` runs at every time step, regardless of the action taken (e.g., gravity, friction).

```rlang
DYNAMICS {
    always {
        // Gravity
        vy = vy - 0.1;
        
        // Position update
        y = y + vy;
        
        // Bounds checking
        if (y < 0.0) {
            y = 0.0;
            crashed = 1; # Yes
        }
    }
}
```

### `when` Block
Logic that runs only when a specific action is chosen.

```rlang
    when (action in [jump]) {
        vy = vy + 1.0;
    }
    
    when (action in [left, right]) {
        // ...
    }
```

### Control Flow
RLang supports `if` statements for logic.

```rlang
    if (x > 10.0) {
        done = 1;
    }
```

## 5. Rewards (`REWARDS`)

Defines the reward function. Rules are evaluated sequentially.

Syntax: `if (condition) -> reward_value;`

```rlang
REWARDS {
    if (crashed == 1) -> -10.0;
    if (x > 9.0) -> 100.0;
    if (done == 0) -> -0.1; // Time penalty
}
```

## 6. Training Configuration (`TRAINING`)

Configures the RL algorithm (PPO, A2C, etc.) and hyperparameters.

```rlang
TRAINING {
    Algo: PPO;
    Timesteps: 50000;
}
```
