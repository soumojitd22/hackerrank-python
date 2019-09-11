"""
chocolate-feast
"""


def chocolate_feast(n, c, m):
    wrappers = n // c
    count = wrappers
    while wrappers >= m:
        chocolates_gained = wrappers // m
        count += chocolates_gained
        wrappers = chocolates_gained + (wrappers % m)

    return count


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolate_feast(n, c, m)
        print(result)
