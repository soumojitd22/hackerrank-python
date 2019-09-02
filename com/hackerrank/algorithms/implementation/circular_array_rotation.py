"""
circular-array-rotation
"""


def circular_array_rotation(a, k, queries):
    return [a[i - k % len(a)] for i in queries]


if __name__ == '__main__':
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circular_array_rotation(a, k, queries)
    print('\n'.join(map(str, result)))
