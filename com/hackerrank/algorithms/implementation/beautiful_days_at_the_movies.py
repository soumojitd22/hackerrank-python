"""
beautiful-days-at-the-movies
"""


def beautiful_days(i, j, k):
    return sum([1 for day in range(i, j + 1) if abs(day - int((str(day)[::-1]))) % k == 0])


if __name__ == '__main__':
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautiful_days(i, j, k)
    print(result)
