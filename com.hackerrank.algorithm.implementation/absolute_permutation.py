"""
absolute-permutation
"""


def absolutePermutation(n, k):
    res = [0 for _ in range(n)]
    for i in range(1, n + 1):
        if (1 <= i - k <= n) and (i - k not in res):
            res[i - 1] = i - k
        elif (1 <= i + k <= n) and (i + k not in res):
            res[i - 1] = i + k
        else:
            return [-1]

    return res


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        result = absolutePermutation(n, k)
        print(' '.join(map(str, result)))
