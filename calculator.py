"""Калькулятор: вычисление выражения вида "a оператор b"."""

import sys

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
    "%": lambda a, b: a % b,
    "^": lambda a, b: a ** b,
}

sys.path.append("libs/matrixlib")
from matrix_io import format_number  # noqa: E402


def calculate(left, operator, right):
    """Выполняет одну арифметическую операцию."""
    if operator not in OPERATIONS:
        raise ValueError(f"неизвестная операция: {operator}")
    if operator in ("/", "//", "%") and right == 0:
        raise ZeroDivisionError("деление на ноль")
    return OPERATIONS[operator](left, right)


def main():
    print("Калькулятор. Поддерживаемые операции: " + " ".join(OPERATIONS))
    print("Введите выражение вида: 12.5 * 4")
    parts = input().split()
    if len(parts) != 3:
        print("Ошибка: ожидается три элемента — число, операция, число")
        return
    try:
        result = calculate(float(parts[0]), parts[1], float(parts[2]))
    except (ValueError, ZeroDivisionError) as error:
        print(f"Ошибка: {error}")
        return
    print(f"{parts[0]} {parts[1]} {parts[2]} = {format_number(result)}")


if __name__ == "__main__":
    main()
