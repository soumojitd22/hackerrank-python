"""
two-characters
"""


def alternate(s):
    uc = tuple(set(list(s)))  # unique chars
    ans = 0
    for i in range(len(uc) - 1):
        for j in range(i + 1, len(uc)):
            t = []
            for c in s:
                if c in (uc[i], uc[j]):
                    t.append(c)
                    if len(t) > 1 and t[-1] == t[-2]:
                        t = []
                        break

            if len(t) > 1:
                ans = max(ans, len(t))

    return ans


if __name__ == "__main__":
    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)
