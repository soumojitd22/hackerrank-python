"""
flatland-space-stations
"""


def flatland_space_stations(n, c):
    if len(c) == 1:
        return max(c[0], n - 1 - c[0])

    c.sort()
    return max(max([(c[i] - c[i - 1]) // 2 for i in range(1, len(c))]), c[0], n - 1 - c[-1])


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatland_space_stations(n, c)
    print(result)
