"""
almost-sorted
"""


def almost_sorted(a):
    s = sorted(a)
    if s == a:
        print("yes")
    else:
        indices = [i for i in range(len(a)) if s[i] != a[i]]
        if len(indices) == 2:
            a[indices[0]], a[indices[1]] = a[indices[1]], a[indices[0]]
            if s == a:
                print("yes")
                print("swap", indices[0] + 1, indices[1] + 1)
            else:
                print("no")
        elif len(indices) > 2:
            a = a[:indices[0]] + a[indices[0]:indices[-1] + 1][::-1] + a[indices[-1] + 1:]
            if s == a:
                print("yes")
                print("reverse", indices[0] + 1, indices[-1] + 1)
            else:
                print("no")
        else:
            print("no")


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    almost_sorted(arr)
