"""
absolute-permutation
"""


def absolutePermutation(n, k):
    if k == 0:
        return [i + 1 for i in range(n)]
    elif n % (2 * k) != 0:
        return [-1]
    else:
        res = [0 for _ in range(n)]
        m = n // (2 * k)
        i = 0
        for _ in range(m):
            for _ in range(k):
                i += 1
                res[i - 1] = i + k

            for _ in range(k):
                i += 1
                res[i - 1] = i - k

        return res


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        result = absolutePermutation(n, k)
        print(' '.join(map(str, result)))
