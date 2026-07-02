HISTORY_FILE = "history.txt"

def show_history():
    try:
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()

        if len(lines) == 0:
            print("NO HISTORY FOUND")
        else:
            for line in reversed(lines):
                print(line.strip())

        file.close()

    except FileNotFoundError:
        print("NO HISTORY FOUND")


def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared")


def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Use format: 8 + 8")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2

    else:
        print("Invalid operator. Use only + - * /")
        return

    if int(result) == result:
        result = int(result)

    print("RESULT:", result)
    save_to_history(user_input, result)


def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")

    while True:
        user_input = input("Enter calculation (+ - * /) or command: ")

        if user_input.lower() == "exit":
            print("Goodbye")
            break

        elif user_input.lower() == "history":
            show_history()

        elif user_input.lower() == "clear":
            clear_history()

        else:
            calculate(user_input)


main()