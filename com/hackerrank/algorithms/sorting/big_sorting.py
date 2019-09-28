"""
big-sorting
"""


def big_sorting(unsorted):
    return sorted(unsorted, key=lambda s: (len(s), s))


if __name__ == "__main__":
    n = int(input())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = big_sorting(unsorted)
    print("\n".join(result))
