"""
counting-valleys
"""


def countingValleys(n, s):
    alt = 0
    v = 0
    for step in s:
        if step == 'U':
            alt += 1
            if alt == 0:
                v += 1
        elif step == 'D':
            alt -= 1

    return v


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)
