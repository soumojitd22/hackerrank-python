"""
between-two-sets
"""


def getTotalX(a, b):
    a_max, b_min, count = max(a), min(b), 0
    for i in range(1, int(b_min / a_max) + 1):
        if (sum((i * a_max) % j for j in a) + sum(j % (i * a_max) for j in b)) == 0:
            count += 1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(str(total))
