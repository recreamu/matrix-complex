"""Поиск максимального элемента матрицы NxM и его индексов."""

import sys

sys.path.append("libs/matrixlib")
from matrix_io import read_matrix, print_matrix, format_number  # noqa: E402


def find_max(matrix):
    """Возвращает максимальный элемент матрицы и его индексы (строка, столбец)."""
    best = matrix[0][0]
    row_index, column_index = 0, 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > best:
                best, row_index, column_index = value, i, j
    return best, row_index, column_index


def main():
    matrix = read_matrix("Исходная матрица")
    print_matrix(matrix, "Введённая матрица")
    value, i, j = find_max(matrix)
    print(f"Максимальный элемент: {format_number(value)}")
    print(f"Индексы (с нуля): строка {i}, столбец {j}")
    print(f"Позиция в матрице: строка {i + 1}, столбец {j + 1}")


if __name__ == "__main__":
    main()
