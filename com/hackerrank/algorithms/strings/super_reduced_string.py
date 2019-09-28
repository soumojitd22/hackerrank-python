"""
super-reduced-string
"""


def super_reduced_string(s):
    r = []
    for c in s:
        if len(r) == 0:
            r.append(c)
        elif c == r[-1]:
            r.pop()
        else:
            r.append(c)

    if len(r) == 0:
        return "Empty String"
    else:
        return "".join(r)


if __name__ == "__main__":
    s = input()
    result = super_reduced_string(s)
    print(result)
