"""
beautiful-triplets
"""
from collections import Counter


def beautiful_triplets(d, arr):
    c = Counter(arr)
    return sum([c[i] * c[i + d] * c[i + 2 * d] for i in c.keys() if i + d in c and i + 2 * d in c])


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautiful_triplets(d, arr)
    print(result)
