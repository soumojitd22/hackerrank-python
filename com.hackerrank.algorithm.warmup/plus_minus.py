"""
plus-minus
"""


def plusMinus(arr):
    length = len(arr)
    gt_zero, lt_zero, zero = 0, 0, 0
    for a in arr:
        if a == 0:
            zero += 1
        elif a > 0:
            gt_zero += 1
        else:
            lt_zero += 1

    print('{0:.6f}'.format(gt_zero / length))
    print('{0:.6f}'.format(lt_zero / length))
    print('{0:.6f}'.format(zero / length))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
