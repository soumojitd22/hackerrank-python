"""
pangrams
"""


def pangrams(s):
    st = set(s.lower())
    ln = 27 if " " in st else 26
    return "pangram" if len(st) == ln else "not pangram"


if __name__ == "__main__":
    s = input()
    result = pangrams(s)
    print(result)
