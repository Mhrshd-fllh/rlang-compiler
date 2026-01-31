import sys
from antlr4 import *
from generated.RLangLexer import RLangLexer
from generated.RLangParser import RLangParser
from semantic_analyzer import SemanticAnalyzer
from codegen.CodeGenerator import CodeGenerator


def main():
    input_file = "test_input.rlang"
    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = RLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)

    tree = parser.prog()
    print(" تحلیل نحوی موفقیت‌آمیز بود.")

    analyzer = SemanticAnalyzer()
    ir = analyzer.analyze(tree)

    if analyzer.errors:
        print("\n خطاهای معنایی یافت شد:")
        for e in analyzer.errors:
            print(f" - {e}")
        return

    print(" تحلیل معنایی موفقیت‌آمیز بود. هیچ خطایی یافت نشد.")

    # --- Code Generation ---
    cg = CodeGenerator(ir)
    output_code = cg.generate()

    output_file = input_file.replace(".rlang", "_env.py")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_code)

    print(f"✅ تولید کد Python محیط RL با موفقیت انجام شد: {output_file}")


if __name__ == "__main__":
    main()
