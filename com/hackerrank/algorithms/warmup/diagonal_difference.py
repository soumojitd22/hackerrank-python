#!/bin/python3

"""
diagonal difference
"""


def diagonalDifference(arr):
    ln = len(arr)
    l_diag = sum([arr[i][i] for i in range(ln)])
    r_diag = sum([arr[i][ln - i - 1] for i in range(ln)])
    return abs(l_diag - r_diag)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(str(result))
