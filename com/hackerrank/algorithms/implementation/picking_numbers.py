"""
picking-numbers
"""
from collections import Counter


def pickingNumbers(a):
    count = 1
    m = Counter(a)
    for i in m.keys():
        if (i + 1 in m) and (m[i] + m[i + 1] > count):
            count = m[i] + m[i + 1]
        elif m[i] > count:
            count = m[i]

    return count


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(str(result))
