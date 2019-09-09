"""
taum-and-bday
"""


def taum_bday(b, w, bc, wc, z):
    if bc + z < wc:
        price = b * bc + w * (bc + z)
    elif wc + z < bc:
        price = w * wc + b * (wc + z)
    else:
        price = b * bc + w * wc

    return price


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        b = int(first_multiple_input[0])
        w = int(first_multiple_input[1])
        second_multiple_input = input().rstrip().split()
        bc = int(second_multiple_input[0])
        wc = int(second_multiple_input[1])
        z = int(second_multiple_input[2])
        result = taum_bday(b, w, bc, wc, z)
        print(result)
