"""
extra-long-factorials
"""


def extra_long_factorials(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    print(factorial)


if __name__ == '__main__':
    n = int(input())
    extra_long_factorials(n)
