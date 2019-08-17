#!/bin/python3

"""
minimum-swaps-2
"""


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    n_arr = [i - 1 for i in arr]
    for i in range(len(n_arr)):
        if i == n_arr[i]:
            continue
        while i != n_arr[i]:
            e = n_arr[i]
            n_arr[i], n_arr[e] = n_arr[e], n_arr[i]
            count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)
