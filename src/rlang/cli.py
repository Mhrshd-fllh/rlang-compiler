import sys
import os
import argparse
from antlr4 import *
from .generated.RLangLexer import RLangLexer
from .generated.RLangParser import RLangParser
from .semantic_analyzer import SemanticAnalyzer
from .codegen.CodeGenerator import CodeGenerator

def main():
    parser = argparse.ArgumentParser(description="RLang Compiler: Compile .rlang files to Python RL environments.")
    parser.add_argument('input_file', help="Path to the .rlang input file")
    parser.add_argument('-o', '--output', default='.', help="Output directory for generated files")
    
    args = parser.parse_args()

    input_path = args.input_file
    output_dir = args.output
    
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_stream = FileStream(input_path, encoding='utf-8')
    lexer = RLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found. Compilation aborted.")
        sys.exit(1)

    print("Parsing successful.")

    analyzer = SemanticAnalyzer()
    try:
        ir = analyzer.analyze(tree)
        print("Semantic analysis successful.")
    except Exception as e:
        print(f"Semantic error: {e}")
        # Print collected errors if any
        for err in analyzer.errors:
            print(f" - {err}")
        sys.exit(1)

    if analyzer.errors:
        print("Semantic errors found:")
        for err in analyzer.errors:
            print(f" - {err}")
        sys.exit(1)

    # Generate Code
    cg = CodeGenerator(ir)
    
    # Determine base filename for output
    base_name = os.path.basename(input_path).replace('.rlang', '')
    env_file = os.path.join(output_dir, f"{base_name}_env.py")
    train_file = os.path.join(output_dir, f"{base_name}_train.py")
    eval_file = os.path.join(output_dir, f"{base_name}_eval.py")

    # Generate Environment
    env_code = cg.generate()
    with open(env_file, "w", encoding="utf-8") as f:
        f.write(env_code)
    print(f"✅ Generated Environment: {env_file}")

    # Generate Training Script
    train_code = cg.generate_training_script(env_filename=os.path.basename(env_file))
    with open(train_file, "w", encoding="utf-8") as f:
        f.write(train_code)
    print(f"✅ Generated Training Script: {train_file}")

    # Generate Eval Script
    eval_code = cg.generate_eval_script(env_filename=os.path.basename(env_file))
    with open(eval_file, "w", encoding="utf-8") as f:
        f.write(eval_code)
    print(f"✅ Generated Evaluation Script: {eval_file}")

if __name__ == '__main__':
    main()
