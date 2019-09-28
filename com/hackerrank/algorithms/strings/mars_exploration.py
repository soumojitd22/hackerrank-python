"""
mars-exploration
"""


def mars_exploration(s):
    count = 0
    for i in range(len(s) // 3):
        if s[3 * i] != 'S':
            count += 1
        if s[3 * i + 1] != 'O':
            count += 1
        if s[3 * i + 2] != 'S':
            count += 1

    return count


if __name__ == "__main__":
    s = input()
    result = mars_exploration(s)
    print(result)
