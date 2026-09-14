"""Сложение двух матриц одинаковой размерности."""

import sys

sys.path.append("libs/matrixlib")
from matrix_io import read_matrix, print_matrix  # noqa: E402
from matrix_ops import check_same_shape  # noqa: E402


def add(a, b):
    """Поэлементно складывает две матрицы одинаковой размерности."""
    n, m = check_same_shape(a, b)
    return [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]


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
