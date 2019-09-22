"""
matrix-layer-rotation
"""


def matrix_rotation(matrix, m, n, r):
    num_layers = min(m, n) // 2
    layers = []
    for i in range(num_layers):
        layer = []
        for j in range(i, m - i):
            layer.append(matrix[j][i])
        for j in range(i + 1, n - i):
            layer.append(matrix[m - i - 1][j])
        for j in range(m - i - 2, i - 1, -1):
            layer.append(matrix[j][n - i - 1])
        for j in range(n - i - 2, i, -1):
            layer.append(matrix[i][j])
        layers.append(layer)

    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(num_layers):
        c = 0
        for j in range(i, m - i):
            result[j][i] = layers[i][(c - r) % len(layers[i])]
            c += 1
        for j in range(i + 1, n - i):
            result[m - i - 1][j] = layers[i][(c - r) % len(layers[i])]
            c += 1
        for j in range(m - i - 2, i - 1, -1):
            result[j][n - i - 1] = layers[i][(c - r) % len(layers[i])]
            c += 1
        for j in range(n - i - 2, i, -1):
            result[i][j] = layers[i][(c - r) % len(layers[i])]
            c += 1

    for rs in result:
        print(' '.join(map(str, rs)))


if __name__ == '__main__':
    mnr = input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrix_rotation(matrix, m, n, r)
