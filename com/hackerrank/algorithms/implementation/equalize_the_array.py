"""
equalize-the-array
"""

from collections import Counter


def equalize_the_array(ar):
    return len(ar) - max(Counter(ar).values())


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = equalize_the_array(arr)
    print(result)
