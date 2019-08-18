"""
birthday_chocolate.
"""


def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[j] for j in range(i, i + m)) == d:
            count += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(str(result))
