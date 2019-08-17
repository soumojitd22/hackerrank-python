"""
day-of-the-programmer
"""


def dayOfProgrammer(year):
    programmers_day = "13.09."
    if year == 1918:
        programmers_day = "26.09."
    elif year < 1918:
        # To check Leap Year : If divisible by 4
        if year % 4 == 0:
            programmers_day = "12.09."
    else:
        # To check Leap Year : If divisible by 400 or divisible by 4 and not divisible by 100
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            programmers_day = "12.09."

    return programmers_day + str(year)


if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)
