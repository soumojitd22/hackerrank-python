"""
find-digits
"""


def find_digits(n):
    num_data = str(n)
    count = 0
    for digit in num_data:
        d = int(digit)
        if d != 0 and n % d == 0:
            count += 1

    return count


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = find_digits(n)
        print(result)
