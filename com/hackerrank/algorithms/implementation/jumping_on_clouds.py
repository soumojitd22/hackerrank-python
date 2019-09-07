"""
jumping-on-clouds
"""


def jumping_on_clouds(c):
    i = 0
    count = 0
    while i < len(c) - 3:
        if c[i + 2] == 1:
            i += 1
        else:
            i += 2
        count += 1

    return count + 1


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumping_on_clouds(c)
    print(result)
