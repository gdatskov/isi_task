"""
You are given a NxM matrix of integer numbers.
We can drop a bomb at anyplace in the matrix, which has the following effect:


    All of the 3 to 8 neighbours (depending on where you
    hit!) of the target are reduced by the value of the target.

    Numbers can be reduced only to 0 - they cannot go to
    negative.


For example, if we have the following matrix:
10 10 10
10  9 10
10 10 10
and we drop bomb at 9, this will result in the following matrix:
1 1 1
1 9 1
1 1 1

Implement a function called matrix_bombing_plan(m).

The function should return a dictionary where keys are positions in the matrix,
represented as tuples, and values are the total sum of the elements of the matrix,
after the bombing at that position.
The positions are the standard indexes, starting from (0, 0)

Input:                                                                 Output:
1 2 3                                                                   {   (0, 0): 42,
4 5 6                                                                       (0, 1): 36,
7 8 9                                                                       (0, 2): 37,
                                                                            (1, 0): 30,
                                                                            (1, 1): 15,
                                                                            (1, 2): 23,
                                                                            (2, 0): 29,
                                                                            (2, 1): 15,
                                                                            (2, 2): 26
                                                                        }
"""


def create_matrix(n, m):
    initial_matrix = {}
    for row in range(n):
        row_input = input().split(' ')

        if len(row_input) != n:
            raise ValueError(f'Invalid row input, {n} numbers required')

        row_numbers = list(map(int, row_input))

        # Create matrix in dictionary format with keys as coordinates
        for number in range(m):
            initial_matrix[(row, number)] = row_numbers[number]

    return initial_matrix


def matrix_bombing_plan(m):
    print('Enter matrix dimentions NxM:')
    rows = int(input('N: '))
    cols = int(input('M: '))
    print(f'Enter {rows} rows with {cols} numbers each, separated by single space')
    matrix = create_matrix(rows, cols)
    target = None
    # Find target:
    for coordinate, value in matrix.items():
        if value == m:
            target = coordinate
    if target is None:
        raise ValueError("Target not found")

    target_row, target_col = target

    start_attack_row = target_row - 1 if (target_row - 1) > 0 else 0
    end_attack_row = target_row + 1 if target_row < rows-1 else target_row
    start_attack_col = target_col - 1 if (target_col - 1) > 0 else 0
    end_attack_col = target_col + 1 if target_col < cols-1 else target_col

    target_value = matrix[target]
    for i in range(start_attack_row, end_attack_row+1):
        for j in range(start_attack_col, end_attack_col+1):
            if matrix[(i, j)] >= target_value:
                matrix[(i, j)] -= target_value
            else:
                matrix[i, j] = 0
    matrix[target] = target_value

    return matrix


print('Enter a value for the target: ')
bomb = int(input())
print(matrix_bombing_plan(bomb))
