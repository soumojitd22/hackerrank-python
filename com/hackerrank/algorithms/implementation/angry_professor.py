"""
angry-professor
"""


def angry_professor(k, a):
    return "NO" if len(list(filter(lambda i: i <= 0, a))) >= k else "YES"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        result = angry_professor(k, a)
        print(result)
