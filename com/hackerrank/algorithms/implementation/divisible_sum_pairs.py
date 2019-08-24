"""
divisible-sum-pairs
"""


def divisible_sum_pairs(n, k, ar):
    return sum(1 for i in range(0, n) for j in range(i + 1, n) if (ar[i] + ar[j]) % k == 0)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisible_sum_pairs(n, k, ar)
    print(result)
