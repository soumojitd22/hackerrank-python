"""
sock-merchant
"""
from collections import Counter


def sockMerchant(n, ar):
    counter = Counter(ar)
    return sum(list(map(lambda v: v // 2, counter.values())))


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
