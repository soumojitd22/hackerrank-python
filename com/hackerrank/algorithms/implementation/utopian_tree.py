"""
utopian-tree
"""


def utopian_tree(n):
    """
    Cycle    Height
    -----    ------
      0         1    =    2 ** 1 - 1
      1         2    =    (2 ** 1 - 1) * 2
      2         3    =    2 ** 2 - 1
      3         6    =    (2 ** 2 - 1) * 2
      4         7    =    2 ** 3 - 1
      5        14    =    (2 ** 3 - 1) * 2
      6        15    =    2 ** 4 - 1
      7        30    =    (2 ** 4 - 1) * 2
      8        31    =    2 ** 5 - 1
    :param n: Cycle number
    :return: Height
    """
    return (2 ** (n // 2 + 1) - 1) * (n % 2 + 1)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopian_tree(n)
        print(result)
