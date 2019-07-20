#!/bin/python3

"""
balanced-brackets
"""

def isBalanced(s):
    m = {'(': ')', '{': '}', '[': ']'}
    stack = list()
    for character in s:
        if character in ('(', '{', '['):
            stack.append(character)
        else:
            if len(stack) == 0:
                return "NO"
            starting_bracket = stack.pop()
            if character != m[starting_bracket]:
                return "NO"

    return "YES" if len(stack) == 0 else "NO"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
