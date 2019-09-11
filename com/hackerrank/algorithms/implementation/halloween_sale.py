"""
halloween-sale
"""


def how_many_games(p, d, m, s):
    games = 0
    while s >= 0:
        s -= p
        p = max(p - d, m)
        games += 1
    return games - 1


if __name__ == '__main__':
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = how_many_games(p, d, m, s)
    print(answer)
