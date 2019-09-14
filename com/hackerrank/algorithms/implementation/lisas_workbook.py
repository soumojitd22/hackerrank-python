"""
lisas-workbook
"""


def workbook(n, k, arr):
    start_page = 1
    count = 0
    for problems in arr:
        end_page = start_page + (problems // k) + (0 if problems % k == 0 else 1) - 1
        start_prob = 1
        for p in range(start_page, end_page + 1):
            end_prob = problems if (start_prob + k - 1) > problems else (start_prob + k - 1)
            if start_prob <= p <= end_prob:
                count += 1
            start_prob = end_prob + 1

        start_page = end_page + 1

    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().split()))
    result = workbook(n, k, arr)
    print(result)
