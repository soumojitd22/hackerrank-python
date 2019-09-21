"""
larrys-array
"""


def larrys_array(a):
    """
    The problem follows a mathematical property - inversion (discrete mathematics).
    If in a set, smaller number exists to right of a bigger number it is called an inversion.
    For this problem if the number of inversions is even then the set can be sorted perfectly.
    But if the number of inversions is odd, this cannot be sorted.
    :param a: Array
    :return: YES if a can be sorted; else NO
    """
    inv = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inv += 1

    return "YES" if inv % 2 == 0 else "NO"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        A = list(map(int, input().rstrip().split()))
        result = larrys_array(A)
        print(result)
