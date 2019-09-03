"""
append-and-delete
"""


def append_and_delete(s, t, k):
    res = "No"
    if len(s) + len(t) <= k:
        res = "Yes"
    else:
        i = 0
        min_length = min(len(s), len(t))
        while i < min_length and s[i] == t[i]:
            i += 1

        unmatched_s = len(s) - i
        unmatched_t = len(t) - i
        unmatched_all = unmatched_s + unmatched_t
        # Why (k - unmatched_all) % 2 ? Because matched characters can also be removed and added back.
        if k >= unmatched_all and (k - unmatched_all) % 2 == 0:
            res = "Yes"

    return res


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())
    result = append_and_delete(s, t, k)
    print(result)
