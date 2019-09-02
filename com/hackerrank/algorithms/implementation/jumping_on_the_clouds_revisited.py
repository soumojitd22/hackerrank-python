"""
jumping-on-the-clouds-revisited
"""


def jumping_on_clouds(c, k):
    n = len(c)
    i = k % n
    e = 100
    while i != 0:
        e = e - 3 if c[i] == 1 else e - 1
        i = (i + k) % n

    # Energy would be lost to jump on last cloud also
    e = e - 3 if c[i] == 1 else e - 1
    return e


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumping_on_clouds(c, k)
    print(result)
