"""
queens-attack-2
"""


def queens_attack(n, k, r_q, c_q, obstacles):
    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1
    up_right = min(up, right)
    up_left = min(up, left)
    down_right = min(down, right)
    down_left = min(down, left)
    for (r_o, c_o) in obstacles:
        if r_o == r_q:
            # For left - right
            if c_o > c_q:
                right = min(c_o - c_q - 1, right)
            else:
                left = min(c_q - c_o - 1, left)

        elif c_o == c_q:
            # For up - down
            if r_o > r_q:
                up = min(r_o - r_q - 1, up)
            else:
                down = min(r_q - r_o - 1, down)

        elif abs(r_o - r_q) / abs(c_o - c_q) == 1:
            # For diagonals
            if r_o > r_q and c_o > c_q:
                # For up - right
                up_right = min(r_o - r_q - 1, up_right)
            elif r_o > r_q and c_o < c_q:
                # For up -left
                up_left = min(r_o - r_q - 1, up_left)
            elif r_o < r_q and c_o < c_q:
                # For down - left
                down_left = min(r_q - r_o - 1, down_left)
            else:
                # For down - right
                down_right = min(r_q - r_o - 1, down_right)

    return up + down + left + right + up_right + up_left + down_left + down_right


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queens_attack(n, k, r_q, c_q, obstacles)
    print(result)
