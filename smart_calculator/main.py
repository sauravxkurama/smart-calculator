from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix
from utils import format_expression, save_to_history, load_history

def main():
    print("🔢 Smart Calculator using Stack (CLI Version)")
    print("⚙️ Supports: +  -  *  /  with brackets ( )")
    print("🧠 Example: 3 + 4 * ( 2 - 1 )\n")

    while True:
        print("\nOptions: [1] Calculate  [2] View History  [3] Exit")
        choice = input("Choose option: ")

        if choice == '1':
            expr = input("🧮 Enter Infix Expression: ")
            expr = format_expression(expr)

            try:
                postfix = infix_to_postfix(expr)
                result = evaluate_postfix(postfix)
                print(f"✅ Postfix: {' '.join(postfix)}")
                print(f"🟢 Result: {result}")
                save_to_history(expr, result)

            except Exception as e:
                print("❌ Error:", str(e))

        elif choice == '2':
            print("\n🕘 Calculation History:")
            history = load_history()
            if history:
                for line in history:
                    print("  ➤", line.strip())
            else:
                print("  (No history yet.)")

        elif choice == '3':
            print("👋 Exiting Calculator. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")
