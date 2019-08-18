#!/bin/python3

"""
2D Array - DS
"""


# Complete the hourglassSum function below.
def hourglassSum(arr):
    v_max = None
    for j in range(4):
        for i in range(4):
            s = arr[j][i] + arr[j][i + 1] + arr[j][i + 2] \
                + arr[j + 1][i + 1] \
                + arr[j + 2][i] + arr[j + 2][i + 1] + arr[j + 2][i + 2]

            if (v_max is None) or (s > v_max):
                v_max = s

    return v_max


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
