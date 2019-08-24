"""
cats-and-a-mouse
"""


def cat_and_mouse(x, y, z):
    cat_a = abs(x - z)
    cat_b = abs(y - z)
    return "Mouse C" if cat_a == cat_b else "Cat A" if cat_a < cat_b else "Cat B"


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = cat_and_mouse(x, y, z)
        print(result)
