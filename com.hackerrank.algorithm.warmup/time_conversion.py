#!/bin/python3

"""
time conversion
"""


def timeConversion(s: str):
    hh, mm, ss = s.split(':')
    zz = "AM" if ss.endswith("AM") else "PM"
    ss = ss.replace(zz, '')
    if hh == "12" and zz == "AM":
        hh = "00"
    elif hh != "12" and zz == "PM":
        hh = str(int(hh) + 12)

    return hh + ":" + mm + ":" + ss


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
