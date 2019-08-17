"""
breaking-best-and-worst-records
"""


def breakingRecords(scores):
    best = worst = scores[0]
    best_counter = worst_counter = 0
    for score in scores[1:]:
        if score > best:
            best = score
            best_counter += 1
        elif score < worst:
            worst = score
            worst_counter += 1

    return best_counter, worst_counter


if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
