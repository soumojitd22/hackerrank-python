"""
minimum-distances
"""


def minimum_distances(a):
    d = dict()
    min_distance = len(a)
    for i in range(len(a)):
        if a[i] in d:
            min_distance = min(abs(d[a[i]] - i), min_distance)
        d[a[i]] = i

    return -1 if min_distance == len(a) else min_distance


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimum_distances(a)
    print(result)
