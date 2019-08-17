"""
find-the-point
"""

n = int(input().strip())
for i in range(n):
    px, py, qx, qy = [int(e) for e in input().strip().split(" ")]
    rx, ry = (qx - px) + qx, (qy - py) + qy
    print(rx, ry, sep=" ")
