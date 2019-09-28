"""
separate-the-numbers
"""


def separate_numbers(s):
    x = -1
    for i in range(1, len(s)):
        y = int(s[:i])
        t = ""
        while len(t) < len(s):
            t += str(y)
            y += 1

        if t == s:
            x = int(s[:i])
            break

    if x == -1:
        print("NO")
    else:
        print("YES", x)


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        s = input()
        separate_numbers(s)
