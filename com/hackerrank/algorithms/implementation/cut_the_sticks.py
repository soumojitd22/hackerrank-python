"""
cut-the-sticks
"""


def cut_the_sticks(a):
    a.sort()
    length_a = len(a)
    return [length_a - i for i in range(length_a) if i == 0 or a[i] != a[i - 1]]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cut_the_sticks(arr)
    print('\n'.join(map(str, result)))
