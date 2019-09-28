"""
hackerrank-in-a-string
"""


def hackerrank_in_a_string(s):
    w = "hackerrank"
    i = 0
    for c in s:
        if c == w[i]:
            if i == len(w) - 1:
                return "YES"
            i += 1

    return "NO"


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrank_in_a_string(s)
        print(result)
