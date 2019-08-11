"""
migratory-birds
"""
from collections import Counter


def migratoryBirds(arr):
    c = Counter(arr)
    mx = max(c.values())
    return [i for i in range(1, 6) if c[i] == mx][0]


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
