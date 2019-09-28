"""
gemstones
"""


def gemstones(arr):
    d = dict()
    for s in arr:
        for c in set(s):
            d[c] = d[c] + 1 if c in d else 1

    return sum([1 for k in d.keys() if d[k] == len(arr)])


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(result)
