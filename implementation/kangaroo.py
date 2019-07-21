#!/bin/python3

"""
kangaroo
"""


def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"
    elif v1 == v2:
        return "NO"

    return "YES" if ((x2 - x1) / (v1 - v2)) > 0 and ((x2 - x1) % (v1 - v2)) == 0 else "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)
