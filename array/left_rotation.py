#!/bin/python3

"""
ctci-array-left-rotation
"""


def rotLeft(a, d):
    return [a[(i + d) % len(a)] for i in range(len(a))]


if __name__ == "__main__":
    n, d = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    print(rotLeft(a, d))
