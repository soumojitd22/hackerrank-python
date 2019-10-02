"""
the-love-letter-mystery
"""


def the_love_letter_mystery(s):
    return sum([abs(ord(s[i]) - ord(s[-(i + 1)])) for i in range(len(s) // 2)])


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = the_love_letter_mystery(s)
        print(result)
