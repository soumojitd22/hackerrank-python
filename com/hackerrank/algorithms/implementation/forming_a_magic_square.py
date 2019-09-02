"""
forming-a-magic-square
"""


def forming_magic_square(s):
    arr = [s[i][j] for i in range(3) for j in range(3)]
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
             [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

    all_sum = [(sum([abs(arr[i] - l[i]) for i in range(9)])) for l in magic]
    return min(all_sum)


if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)
    print(result)
