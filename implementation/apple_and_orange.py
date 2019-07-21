#!/bin/python3

"""
apple and orange
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_positions = [apple + a for apple in apples]
    orange_positions = [orange + b for orange in oranges]
    print(len(list(filter(lambda x: s <= x <= t, apple_positions))))
    print(len(list(filter(lambda x: s <= x <= t, orange_positions))))


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
