"""
strong-password
"""


def minimum_number(n, password):
    count = [0, 0, 0, 0]
    for c in password:
        if c in "0123456789":
            count[0] = 1
        elif c in "abcdefghijklmnopqrstuvwxyz":
            count[1] = 1
        elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count[2] = 1
        elif c in "!@#$%^&*()-+":
            count[3] = 1

    return max(4 - sum(count), 6 - n)


if __name__ == "__main__":
    n = int(input())
    password = input()
    answer = minimum_number(n, password)
    print(answer)
