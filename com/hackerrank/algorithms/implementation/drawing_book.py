"""
drawing-book
"""


def pageCount(n, p):
    if p == 1 or p == n:
        return 0

    forward = (p - 1) // 2 + (p - 1) % 2
    backward = (n - p) // 2 + (n - p) % 2 if n % 2 == 0 else (n - 1 - p) // 2 + (n - 1 - p) % 2
    return min(forward, backward)


if __name__ == '__main__':
    n = int(input())
    p = int(input())
    print(-1 % 2)
    result = pageCount(n, p)
    print(result)
