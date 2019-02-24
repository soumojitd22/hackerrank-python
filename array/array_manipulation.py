#!/bin/python3

"""
array-manipulation
"""


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    max_num = x = 0
    for q in queries:
        a, b, k = q
        arr[a - 1] += k
        if b - 1 < len(arr):
            arr[b - 1] -= k

    for i in arr:
        x += i
        if max_num < x:
            max_num = x

    return max_num


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
