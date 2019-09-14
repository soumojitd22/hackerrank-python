"""
strange-counter
"""
from math import ceil, log


def strange_counter(t):
    """
    Cycle   counter     time
    -----   -------     ----
      0        3          1
               2          2
               1          3 = 3 * (2 ** 0)
    -------------------------
      1        6          4
               5          5
               4          6
               3          7
               2          8
               1          9 = 3 * (2 ** 0 + 2 ** 1)
    -------------------------
      2       12         10
              11         11
              13         12
              ..............
              ..............
               1         21 = 3 * (2 ** 0 + 2 ** 1 + 2 ** 2)
    -------------------------
      3       24         22
              23         23
              ..............
              ..............
               1         45 = 3 * (2 ** 0 + 2 ** 1 + 2 ** 2 + 2 ** 3)
    -------------------------
    The last counter of a cycle, i.e., 1 occurs at t = Sum of GP series = 3 * (2 ** n - 1) / ( 2 - 1) = 3 * 2 ** n - 3
    So the cycle number, n = log((t + 3) / 3, base=2) = log(t / 3 + 1, base=2)
    Now n would be perfect number if t = t_cycle_max (max time of a cycle)
    For any other value of t of a particular cycle would return fractional number
    So we need to apply ceil function to get the actual value of n.
    :param t: time
    :return: counter
    """
    n = ceil(log(t / 3 + 1, 2))
    t_cycle_max = 3 * (2 ** n - 1)
    return t_cycle_max - t + 1


if __name__ == '__main__':
    t = int(input())
    result = strange_counter(t)
    print(result)
