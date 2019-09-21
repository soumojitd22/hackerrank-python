"""
emas-supercomputer
"""


def two_pluses(n, m, grid):
    res = 0
    g = [list(s) for s in grid]
    # Iterate over each point
    for x1 in range(n):
        for y1 in range(m):
            # Check if the point is 'G'
            if g[x1][y1] == 'G':
                plus_length1 = 0
                # Check all possible pluses for (x1, y1)
                while x1 + plus_length1 < n and g[x1 + plus_length1][y1] == 'G' \
                        and x1 - plus_length1 >= 0 and g[x1 - plus_length1][y1] == 'G' \
                        and y1 + plus_length1 < m and g[x1][y1 + plus_length1] == 'G' \
                        and y1 - plus_length1 >= 0 and g[x1][y1 - plus_length1] == 'G':
                    g[x1 + plus_length1][y1] = '+'
                    g[x1 - plus_length1][y1] = '+'
                    g[x1][y1 + plus_length1] = '+'
                    g[x1][y1 - plus_length1] = '+'
                    # Check for other non-overlapping plus
                    for x2 in range(n):
                        for y2 in range(m):
                            if g[x2][y2] == 'G':
                                plus_length2 = 0
                                while x2 + plus_length2 < n and g[x2 + plus_length2][y2] == 'G' \
                                        and x2 - plus_length2 >= 0 and g[x2 - plus_length2][y2] == 'G' \
                                        and y2 + plus_length2 < m and g[x2][y2 + plus_length2] == 'G' \
                                        and y2 - plus_length2 >= 0 and g[x2][y2 - plus_length2] == 'G':
                                    res = max(res, (4 * plus_length1 + 1) * (4 * plus_length2 + 1))
                                    plus_length2 += 1

                    plus_length1 += 1

                plus_length1 = 0
                while x1 + plus_length1 < n and g[x1 + plus_length1][y1] == '+' \
                        and x1 - plus_length1 >= 0 and g[x1 - plus_length1][y1] == '+' \
                        and y1 + plus_length1 < m and g[x1][y1 + plus_length1] == '+' \
                        and y1 - plus_length1 >= 0 and g[x1][y1 - plus_length1] == '+':
                    g[x1 + plus_length1][y1] = 'G'
                    g[x1 - plus_length1][y1] = 'G'
                    g[x1][y1 + plus_length1] = 'G'
                    g[x1][y1 - plus_length1] = 'G'
                    plus_length1 += 1

    return res


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = two_pluses(n, m, grid)
    print(result)
