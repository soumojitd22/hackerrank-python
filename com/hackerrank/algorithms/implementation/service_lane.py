"""
service-lane
"""


def service_lane(width, cases):
    return [min(width[i:j + 1]) for (i, j) in cases]


if __name__ == '__main__':
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = service_lane(width, cases)
    print('\n'.join(map(str, result)))
