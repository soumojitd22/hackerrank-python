"""
absolute-permutation
"""


def absolutePermutation(n, k):
    """
    We need to return lexicographically smallest absolute permutation.
    Suppose N = 8; n = [1, 2, 3, 4, 5, 6, 7, 8]
    and k = 2
    Now we can blindly say that the first number of the return array would be 1 + 2 = 3;
    (that's why we could get 3 - 1 = 2)
    Second element - 2 + 2 = 4
    Now the third element could be 3 + 2 = 5 or 3 - 2 = 1
    But if we choose 3 - 2 = 1, we could get lexicographically smallest absolute permutation.
    Again for 5, 5 + 2 = 7 and 5 - 2 = 3 are possible outputs but we cannot choose 5 - 2 = 3 since it is already
    occurred for position 1

    So,
      n      k    r
    -----  ----- ----
      1     +2    3
      2     +2    4
      3     -2    1
      4     -2    2
      5     +2    7
      6     +2    8
      7     -2    5
      8     -2    6

    So for first k the position is added with +k, and for next k the position is added with -k and so on.
    So if n % (2 * k) != 0, the absolute permutation is not possible.
    :param n: Array
    :param k: Difference
    :return: Permuted array
    """
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
