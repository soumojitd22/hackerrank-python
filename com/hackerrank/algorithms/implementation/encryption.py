"""
encryption
"""
from math import ceil, sqrt


def encryption(s):
    ln = len(s)
    col = ceil(sqrt(ln))
    return ' '.join(list(map(lambda r: ''.join(r),
                             [[s[c + r * col] for r in range(col) if (c + r * col) < ln] for c in range(col)])))


if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)
