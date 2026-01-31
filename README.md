# RLang Compiler

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)

**RLang** is a Domain Specific Language (DSL) designed to simplify the creation of Reinforcement Learning (RL) environments. The **RLang Compiler** takes high-level environment descriptions (`.rlang` files) and compiles them into fully functional Python code compatible with Gymnasium and Stable-Baselines3.

## Motive 🎯

Creating RL environments often involves writing repetitive boilerplate code for state spaces, action spaces, and stepping logic. RLang abstracts this complexity, allowing researchers and developers to focus on the **dynamics** and **reward functions** of their environments.

## Features ✨

*   **Concise Syntax**: Define states, actions, and physics in a readable format.
*   **Automatic Gym Integration**: Generates `gymnasium.Env` classes automatically.
*   **Built-in Initializers**: Validates semantics and generates training scripts.
*   **Control Flow**: Supports `always`, `when`, and `if` logic for complex dynamics.
*   **Reward Shaping**: Define multiple reward conditions easily.

## Requirements 📦

*   Python 3.9+
*   Dependencies (installed automatically):
    *   `antlr4-python3-runtime`
    *   `numpy`
    *   `gymnasium`
    *   `stable-baselines3`
    *   `shimmy`

## Installation 🛠️

Clone the repository and install the package:

```bash
git clone https://github.com/your-username/rlang-compiler.git
cd rlang-compiler
pip install .
```

For development (editable mode):

```bash
pip install -e .
```

## Usage 🚀

Once installed, use the `rlang` command to compile your models.

### Command Structure
```bash
rlang <input_file.rlang> [-o OUTPUT_DIR]
```

### Example: Alien Lander 🛸

We include a verified example of a physics-based landing task.

1.  **Compile the Model**:
    ```bash
    rlang examples/alien_lander.rlang -o build
    ```

    This generates three files in the `build/` directory:
    *   `alien_lander_env.py`: The Gymnasium environment.
    *   `alien_lander_train.py`: A PPO training script.
    *   `alien_lander_eval.py`: A visual evaluation script.

2.  **Train the Agent**:
    ```bash
    python build/alien_lander_train.py
    ```

3.  **Evaluate the Agent**:
    ```bash
    python build/alien_lander_eval.py
    ```

## Project Structure 📂

*   `src/rlang/`: Source code for the compiler (CLI, Semantic Analyzer, Code Generator).
*   `examples/`: Sample `.rlang` files (e.g., Alien Lander).
*   `grammers/`: ANTLR4 grammar definitions.

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request.

## License 📄

This project is licensed under the MIT License.
