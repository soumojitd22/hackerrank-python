"""
caesar-cipher
"""


def caesar_cipher(s, k):
    r = ''
    for c in s:
        if c.isalpha():
            a = ord('A') if c.isupper() else ord('a')
            r += chr(a + (ord(c) - a + k) % 26)
        else:
            r += c

    return str(r)


if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())
    result = caesar_cipher(s, k)
    print(result)
