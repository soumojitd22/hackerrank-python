"""
fair-ration
"""


def fairRations(B):
    if sum(B, 0) % 2 != 0:
        return "NO"
    count = 0
    i = 0
    while i < len(B) - 1:
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            count += 2
        i += 1
    return count


if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
