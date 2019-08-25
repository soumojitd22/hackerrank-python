"""
electronics-shop
"""


def get_money_spent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    max_spent = -1
    for i in range(len(keyboards)):
        j = 0
        if keyboards[i] + drives[j] < max_spent:
            return max_spent
        while j < len(drives) and keyboards[i] + drives[j] > b:
            j += 1
        if j < len(drives):
            spent = keyboards[i] + drives[j]
            max_spent = max(spent, max_spent)

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
