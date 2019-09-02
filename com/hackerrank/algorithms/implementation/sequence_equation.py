"""
sequence-equation
"""


def permutation_equation(p):
    res = [0 for _ in p]
    for i in p:
        res[p[p[i - 1] - 1] - 1] = i

    return res


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutation_equation(p)
    print('\n'.join(map(str, result)))
