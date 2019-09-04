"""
sherlock-and-squares
"""
import math


def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return y - x + 1


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        result = squares(a, b)
        print(result)
