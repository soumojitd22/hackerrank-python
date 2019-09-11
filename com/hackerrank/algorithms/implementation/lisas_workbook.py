"""
lisas-workbook
"""


def workbook(n, k, arr):
    page = 1
    special = 0
    for p in arr:
        for i in range(1, p + 1):
            if i == page:
                special += 1
            if i % k == 0:
                page += 1

        if p % k != 0:
            page += 1

    return special


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
