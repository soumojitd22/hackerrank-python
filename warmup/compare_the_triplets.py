"""
compare-the-triplets
"""


def compareTriplets(a, b):
    r = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            r[0] += 1
        elif b[i] > a[i]:
            r[1] += 1

    return r


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))
