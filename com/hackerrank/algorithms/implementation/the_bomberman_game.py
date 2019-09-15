"""
the-bomberman-game
"""


def bomber_man(n, r, c, grid):
    """
    n = 1 --> Nothing happens
    n = 2, 4, 6, 8, ....(any even) --> bomberman fills up the empty places with bombs.
                                      So the grid would be full of bombs.
    n = 3 --> Bombs placed at n = 1 will detonate
    n = 5 --> After detonation at n = 3, remaining bombs will detonate. So to determine grid after n = 5,
              we need to first determine grid after n = 3.
    n = 7, 11, 15, 19, ....(n % 4 == 3) --> The grid looks same as after n = 3
    n = 9, 13, 17, 21, ....(n % 4 == 1) --> The grid looks same as after n = 5
    :param n: Time
    :param r: Row
    :param c: Column
    :param grid: Grid
    :return: Grid after Time n
    """
    res = []
    if n == 1:
        res = grid
    elif n % 2 == 0:
        res = ['O' * c for _ in range(r)]
    elif n % 4 == 3:
        res = after_bomb_detonate(r, c, grid)
    elif n % 4 == 1:
        n3 = after_bomb_detonate(r, c, grid)
        res = after_bomb_detonate(r, c, n3)

    return res


def after_bomb_detonate(r, c, g):
    """
    If a bomb exists at any of the below mentioned points, the point under consideration would be impacted -
    The point itself
    Up
    Down
    Right
    Left
    :param r: Row
    :param c: Column
    :param g: Grid
    :return: Grid after bomb detonation
    """
    temp = []
    for i in range(r):
        s = []
        for j in range(c):
            if g[i][j] == 'O' \
                    or (i + 1 < r and g[i + 1][j] == 'O') \
                    or (i - 1 >= 0 and g[i - 1][j] == 'O') \
                    or (j + 1 < c and g[i][j + 1] == 'O') \
                    or (j - 1 >= 0 and g[i][j - 1] == 'O'):
                s.append('.')
            else:
                s.append('O')

        temp.append(''.join(s))

    return temp


if __name__ == '__main__':
    rcn = input().split()
    r = int(rcn[0])
    c = int(rcn[1])
    n = int(rcn[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomber_man(n, r, c, grid)
    print('\n'.join(result))
