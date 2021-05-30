#!/bin/python3

"""
ctci-array-left-rotation
"""


def rot_left(a, d):
    return [a[(i + d) % len(a)] for i in range(len(a))]


if __name__ == "__main__":
    n, d = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    print(*rot_left(a, d), end=' ')
