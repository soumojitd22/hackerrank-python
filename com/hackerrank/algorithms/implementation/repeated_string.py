"""
repeated-string
"""


def repeated_string(s, n):
    return s.count('a') * (n // len(s)) + s.count('a', 0, n % len(s))


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeated_string(s, n)
    print(result)
