"""
happy-ladybugs
"""
from collections import Counter


def happy_ladybugs(b):
    if len(b) == 1:
        return "YES" if b == '_' else "NO"
    elif '_' in b:
        count = Counter(b)
        for i in count.keys():
            if i != '_' and count[i] == 1:
                return "NO"
        return "YES"
    else:
        for i in range(1, len(b) - 1):
            if b[i] != b[i - 1] and b[i] != b[i + 1]:
                return "NO"
        return "NO" if b[-1] != b[-2] else "YES"


if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happy_ladybugs(b)
        print(result)
