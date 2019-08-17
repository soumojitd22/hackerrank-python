"""
picking-numbers
"""


def pickingNumbers(a):
    m = {}
    count = 1
    for i in a:
        if i in m:
            m[i] += 1
            count = m[i] if count < m[i] else count
        else:
            m[i] = 1

    for i in m.keys():
        if (i + 1 in m) and (m[i] + m[i + 1] > count):
            count = m[i] + m[i + 1]

    return count


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(str(result))
