"""
acm-icpc-team
"""


def acm_team(n, m, topic):
    max_skills = 0
    max_skill_teams = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            skill_sets = str(bin((int(topic[i], 2) | int(topic[j], 2))))[2:].count('1')
            if skill_sets > max_skills:
                max_skill_teams = 1
                max_skills = skill_sets
            elif skill_sets == max_skills:
                max_skill_teams += 1

    return max_skills, max_skill_teams


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acm_team(n, m, topic)
    print('\n'.join(map(str, result)))
