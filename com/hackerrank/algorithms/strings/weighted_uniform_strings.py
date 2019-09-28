"""
weighted-uniform-strings
"""


def weighted_uniform_strings(s, q):
    counts = [ord(s[0]) - ord('a') + 1]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counts.append(counts[-1] + (ord(s[i]) - ord('a') + 1))
        else:
            counts.append(ord(s[i]) - ord('a') + 1)

    counts = set(counts)
    return ["Yes" if i in counts else "No" for i in q]


if __name__ == "__main__":
    s = input()
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weighted_uniform_strings(s, queries)
    print("\n".join(result))
