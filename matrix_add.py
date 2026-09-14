"""Сложение двух матриц одинаковой размерности."""

import sys

sys.path.append("libs/matrixlib")
from matrix_io import read_matrix, print_matrix  # noqa: E402


def add(a, b):
    """Поэлементно складывает две матрицы."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("сложение определено только для матриц одинаковой размерности")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def main():
    first = read_matrix("Первая матрица")
    second = read_matrix("Вторая матрица")
    try:
        result = add(first, second)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    print_matrix(first, "Матрица A")
    print_matrix(second, "Матрица B")
    print_matrix(result, "Сумма A + B")


if __name__ == "__main__":
    main()
