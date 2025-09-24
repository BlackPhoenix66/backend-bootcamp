from calculator import add, subtract, multiply, divide

OPS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def main():
    print("Калькулятор (пример). Формат: число оператор число. exit чтобы выйти")
    while True:
        line = input("> ").strip()
        if not line:
            continue
        if line.lower() in ("exit", "quit"):
            print('Выход')
            break

        try:
            a_str, op, b_str = line.split()
            a = float(a_str)
            b = float(b_str)
            if op not in OPS:
                print("Неизвестный оператор:", op)
                continue
            res = OPS[op](a, b)
            print("=>", res)
        except ValueError as e:
            print("Ошибка", e)
        except Exception:
            print("Неправильный формат. Пример: 2 + 3")

if __name__ == "__main__":
    main()