"""
viral-advertising
"""


def viral_advertising(n):
    viral_count = 2
    days_viral = 2
    for _ in range(1, n):
        days_viral = (days_viral * 3) // 2
        viral_count += days_viral

    return viral_count


if __name__ == '__main__':
    n = int(input())
    result = viral_advertising(n)
    print(result)
