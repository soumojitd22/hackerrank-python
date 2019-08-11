"""
min-max-sum
"""


def miniMaxSum(arr):
    max_value = arr[0]
    min_value = arr[0]
    sum_arr = 0
    for a in arr:
        if a > max_value:
            max_value = a
        elif a < min_value:
            min_value = a

        sum_arr += a

    min_sum = sum_arr - max_value
    max_sum = sum_arr - min_value
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
