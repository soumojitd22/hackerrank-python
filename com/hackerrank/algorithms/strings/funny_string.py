"""
funny-string
"""


def funny_string(s):
    r = "Funny"
    for i in range((len(s) - 1) // 2):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[len(s) - 1 - i]) - ord(s[len(s) - 2 - i])):
            r = "Not Funny"
            break

    return r


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = funny_string(s)
        print(result)
