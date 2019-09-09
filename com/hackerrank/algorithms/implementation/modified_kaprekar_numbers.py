"""
modified-kaprekar-numbers
"""


def kaprekar_numbers(p, q):
    k_nums = []
    for i in range(p, q + 1):
        num = str(i)
        d = len(num)
        squared_num = str(i ** 2)
        sd = len(squared_num)
        right = int(squared_num[sd - d:])
        left = int("0" if sd - d == 0 else squared_num[:sd - d])
        if left + right == i:
            k_nums.append(num)

    print(" ".join(k_nums) if len(k_nums) > 0 else "INVALID RANGE")


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekar_numbers(p, q)
