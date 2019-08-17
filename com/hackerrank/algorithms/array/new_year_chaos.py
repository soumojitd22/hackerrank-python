#!/bin/python3

"""
new-year-chaos
"""


def minimumBribes(q):
    len_q = len(q)
    min_most = [len_q + 1, len_q + 2]
    bribe_count = 0
    for i in range(len_q - 1, -1, -1):
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return
        if q[i] > min_most[1]:
            bribe_count += 2
        elif q[i] > min_most[0]:
            bribe_count += 1
            min_most[1] = q[i]
        else:
            min_most[1] = min_most[0]
            min_most[0] = q[i]

    print(bribe_count)


if __name__ == "__main__":
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
