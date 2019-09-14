"""
cavity-map
"""


def cavity_map(grid):
    n = len(grid)
    for r in range(1, n - 1):
        s = list(grid[r])
        sp = list(grid[r - 1])
        sn = list(grid[r + 1])
        for c in range(1, n - 1):
            if ord(s[c]) > ord(s[c + 1]) and ord(s[c]) > ord(sp[c]) \
                    and ord(s[c]) > ord(s[c - 1]) and ord(s[c]) > ord(sn[c]):
                s[c] = 'X'
                grid[r] = ''.join(s)

    return grid


if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavity_map(grid)
    print('\n'.join(result))
