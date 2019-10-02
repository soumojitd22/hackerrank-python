"""
alternating-characters
"""


def alternating_characters(s):
    return sum([1 for i in range(len(s) - 1) if s[i] == s[i + 1]])


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternating_characters(s)
        print(result)
