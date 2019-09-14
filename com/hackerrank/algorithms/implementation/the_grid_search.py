"""
the-grid-search
"""


def grid_search(g, p):
    for gi in range(len(g) - len(p) + 1):
        index = g[gi].find(p[0])
        if index != -1:
            indices = [index]
            while index != -1:
                index = g[gi].find(p[0], index + 1)
                if index != -1:
                    indices.append(index)

            for idx in indices:
                if len([1 for pi in range(1, len(p)) if g[gi + pi].startswith(p[pi], idx)]) == len(p) - 1:
                    return "YES"

    return "NO"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = grid_search(G, P)
        print(result)
