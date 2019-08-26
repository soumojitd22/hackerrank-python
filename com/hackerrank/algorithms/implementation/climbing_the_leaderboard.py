"""
climbing-the-leaderboard
"""


def climbing_leaderboard(scores, alice):
    result = []
    ranks = [scores[0]]
    for i in range(1, len(scores)):
        if scores[i] != scores[i - 1]:
            ranks.append(scores[i])

    j = len(ranks) - 1
    for i in range(len(alice)):
        while j >= 0 and alice[i] > ranks[j]:
            j -= 1

        if j == -1:
            result.append(1)
        elif alice[i] == ranks[j]:
            result.append(j + 1)
        else:
            result.append(j + 2)

    return result


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbing_leaderboard(scores, alice)
    print('\n'.join(map(str, result)))
