"""
non-divisible-subset
"""


def non_divisible_subset(k, s):
    count = 0
    remainder_arr = [0 for _ in range(k)]
    for i in s:
        remainder_arr[i % k] += 1

    if remainder_arr[0] > 0:
        count += 1

    for i in range(1, k // 2 + 1):
        if i == k // 2 and k % 2 == 0 and remainder_arr[k // 2] > 0:
            count += 1
        else:
            count += max(remainder_arr[i], remainder_arr[k - i])

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = non_divisible_subset(k, s)
    print(result)
