"""Суммы элементов каждой строки и каждого столбца матрицы NxM."""

import sys

sys.path.append("libs/matrixlib")
from matrix_io import read_matrix, print_matrix, format_number  # noqa: E402


def row_sums(matrix):
    """Возвращает список сумм элементов по строкам."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Возвращает список сумм элементов по столбцам."""
    return [sum(column) for column in zip(*matrix)]


def main():
    matrix = read_matrix("Исходная матрица")
    print_matrix(matrix, "Введённая матрица")
    for i, value in enumerate(row_sums(matrix), start=1):
        print(f"Сумма строки {i}: {format_number(value)}")
    for j, value in enumerate(column_sums(matrix), start=1):
        print(f"Сумма столбца {j}: {format_number(value)}")


if __name__ == "__main__":
    main()
