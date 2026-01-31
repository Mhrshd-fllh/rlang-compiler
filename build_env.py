from antlr4 import FileStream, CommonTokenStream
from generated.RLangLexer import RLangLexer
from generated.RLangParser import RLangParser

from semantic_analyzer import SemanticAnalyzer
from codegen.CodeGenerator import  CodeGenerator
from symbol_table import SymbolTable, Type  # مطمئن شوید Type از symbol_table ایمپورت می‌شود


def main():

    rlang_file_path = "test_input.rlang"

    # --- 2. Phase 1 & 2: Parsing ---
    try:
        input_stream = FileStream(rlang_file_path)
    except FileNotFoundError:
        print(f"❌ خطا: فایل '{rlang_file_path}' پیدا نشد. مطمئن شوید فایل در مسیر صحیح قرار دارد.")
        print("💡 راه حل: فایل example.rlang را کنار build_env.py قرار دهید یا مسیر آن را در build_env.py اصلاح کنید.")
        return

    lexer = RLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RLangParser(token_stream)

    # ⚠️ ⚠️ ⚠️ مهمترین قسمت: اسم این متد باید دقیقاً همان START RULE گرامر شما باشد.
    # اگر rule اول گرامر شما 'rlangProgram' است، اینجا بنویسید parser.rlangProgram()
    # اگر 'program' است، بنویسید parser.program()
    # اگر 'model' است، بنویسید parser.model()
    # لطفاً فقط همین یک خط را بعد از اجرا (اگر خطا داد) بر اساس اولین rule گرامرتان اصلاح کنید.
    tree = parser.prog()  # <--- این خط را بررسی و در صورت نیاز اصلاح کنید

    # --- 3. Phase 3: Semantic Analysis ---
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)

    if analyzer.errors:
        print("❌ خطاهای معنایی یافت شد:")
        for error in analyzer.errors:
            print(f"- {error}")
        return
    else:
        print("✅ تحلیل معنایی با موفقیت انجام شد.")

    # --- 4. Phase 4: Code Generation ---
    codegen = CodeGenerator(analyzer.symbol_table)
    code = codegen.generate()

    # --- 5. ذخیره env.py ---
    with open("env.py", "w") as f:
        f.write(code)

    print("✅ env.py با موفقیت تولید شد.")


if __name__ == "__main__":
    main()
