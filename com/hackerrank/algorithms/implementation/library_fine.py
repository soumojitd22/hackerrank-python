"""
library-fine
"""


def library_fine(dr, mr, yr, de, me, ye):
    if yr < ye:
        fine = 0
    elif yr == ye and mr < me:
        fine = 0
    elif yr == ye and mr == me and dr <= de:
        fine = 0
    elif yr > ye:
        fine = 10000
    elif mr > me:
        fine = 500 * (mr - me)
    else:
        fine = 15 * (dr - de)

    return fine


if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])
    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])
    result = library_fine(d1, m1, y1, d2, m2, y2)
    print(result)
