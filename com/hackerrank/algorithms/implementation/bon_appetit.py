"""
bon-appetit
"""


def bonAppetit(bill, k, b):
    anna_bill = sum([amt for (i, amt) in enumerate(bill) if i != k]) // 2
    print("Bon Appetit" if b == anna_bill else (b - anna_bill))


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
