"""
organizing-containers-of-balls
"""


def organizing_containers(c):
    d = dict()
    n = len(c)
    for i in range(n):
        total_of_a_type = 0
        for j in range(n):
            total_of_a_type += c[j][i]
        d[total_of_a_type] = i

    for i in range(n):
        total_of_a_container = 0
        for j in range(n):
            total_of_a_container += c[i][j]
        if total_of_a_container not in d:
            return "Impossible"

    return "Possible"


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizing_containers(container)
        print(result)
