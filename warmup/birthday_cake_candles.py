#!/bin/python3

"""
birthday-cake-candles
"""


def birthdayCakeCandles(ar):
    return ar.count(max(ar))


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(str(result))
