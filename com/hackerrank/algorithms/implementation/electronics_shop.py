"""
electronics-shop
"""


def get_money_spent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    max_spent = -1
    for keyboard in keyboards:
        j = 0
        if keyboard + drives[j] < max_spent:
            return max_spent
        while j < len(drives) and keyboard + drives[j] > b:
            j += 1
        if j < len(drives):
            max_spent = max(max_spent, keyboard + drives[j])

    return max_spent


if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = get_money_spent(keyboards, drives, b)
    print(moneySpent)
