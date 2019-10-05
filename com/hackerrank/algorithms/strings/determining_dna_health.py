"""
determining-dna-health
"""

import bisect
import math
from collections import defaultdict

"""
Note: Accessing a list using indexing like l[0] and l[1] is costlier operation than a, b = l.
May be a, b = l uses caches optimally

This is the only trick I got to solve this problem within permissible time.
I tried to solve using Aho-Corasick algorithm first, but Test cases 7, 8, 9 and 13 were failing.
Test case 13 would fail if the above mentioned 'Note' is not followed.

Algorithm of the solution:
First memorize the genes - 
Create a dictionary to hold 
{key = the gene words; value = list of (list of (gene id) and list of (1-indexed cumulative health score))}
Create a set of subsequences of gene word; E.g. - if gene word = abc, the set would store {a, ab, abc, b, bc, c}

Inside the get_health method -
We get all possible sequences from the strand _d, at the line seq = _d[i:j]
If the sequence is not present in the set of subsequences, we know that using the sequence no gene word can be formed
So we break the inner loop and go to next character to start with.

Now bisect used to efficiently get index where the number x can be placed in a sorted list L
bisect(L, x)

The line 
(cum_h[right] - cum_h[left])
gives the sum of the health scores from gid = left to gid = right
"""


def memorize_genes(_genes, _health):
    _memory = defaultdict(lambda: [[], [0]])
    _sub_seqs = set()
    for gid, gene in enumerate(_genes):
        _memory[gene][0].append(gid)
        _memory[gene][1].append(_memory[gene][1][-1] + _health[gid])
        for i in range(1, len(gene) + 1):
            _sub_seqs.add(gene[:i])

    return _memory, _sub_seqs


def get_health(_d, _first, _last, _memory, _sub_seqs):
    health_score = 0
    len_d = len(_d)
    for i in range(len_d):
        for j in range(i + 1, len_d + 1):
            seq = _d[i:j]
            if seq not in _sub_seqs:
                break
            if seq not in _memory:
                continue
            gid, cum_h = _memory[seq]
            left = bisect.bisect_left(gid, _first)
            right = bisect.bisect_right(gid, _last, lo=left)
            health_score += (cum_h[right] - cum_h[left])

    return health_score


if __name__ == '__main__':
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    memory, sub_seqs = memorize_genes(genes, health)
    s = int(input())
    max_health = 0
    min_health = math.inf
    for s_itr in range(s):
        first, last, d = input().split()
        first = int(first)
        last = int(last)
        h = get_health(d, first, last, memory, sub_seqs)
        max_health = max(max_health, h)
        min_health = min(min_health, h)

    print(min_health, max_health)
