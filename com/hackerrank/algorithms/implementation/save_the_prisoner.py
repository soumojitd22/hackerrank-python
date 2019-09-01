"""
save-the-prisoner
"""


def save_the_prisoner(n, m, s):
    return n if (s + m - 1) % n == 0 else (s + m - 1) % n


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nms = input().split()
        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])
        result = save_the_prisoner(n, m, s)
        print(result)
