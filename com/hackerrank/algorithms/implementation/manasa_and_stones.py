"""
manasa-and-stones
"""


def stones(n, a, b):
    if a == b:
        return [(n - 1) * a]

    a, b = min(a, b), max(a, b)
    return [(n - 1 - i) * a + i * b for i in range(n)]


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(' '.join(map(str, result)))
