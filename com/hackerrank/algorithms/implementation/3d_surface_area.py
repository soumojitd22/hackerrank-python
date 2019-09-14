"""
3d-surface-area
"""


def surface_area(a, h, w):
    """
    Top and bottom surface area would be fully uncovered.
    So W * H for top surface area and another W * H for bottom surface area.
    :param a: Array
    :param h: Height of Array a
    :param w: Width of Array a
    :return: Total surface area
    """
    area = 2 * h * w
    for h_id in range(h):
        for w_id in range(w):
            # up
            area += max(0, a[h_id][w_id] - (a[h_id - 1][w_id] if h_id - 1 >= 0 else 0))
            # down
            area += max(0, a[h_id][w_id] - (a[h_id + 1][w_id] if h_id + 1 < h else 0))
            # left
            area += max(0, a[h_id][w_id] - (a[h_id][w_id - 1] if w_id - 1 >= 0 else 0))
            # right
            area += max(0, a[h_id][w_id] - (a[h_id][w_id + 1] if w_id + 1 < w else 0))

    return area


if __name__ == '__main__':
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surface_area(A, H, W)
    print(result)
