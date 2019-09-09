"""
bigger-is-greater
"""


def bigger_is_greater(w):
    bigger_word = "no answer"
    ln = len(w)
    arr = list(w)
    if ln > 1:
        i = ln - 1
        while i - 1 >= 0 and arr[i] <= arr[i - 1]:
            i -= 1

        char_pos1 = i - 1
        if char_pos1 != -1:
            i = ln - 1
            while i >= char_pos1 + 1 and arr[i] <= arr[char_pos1]:
                i -= 1

            char_pos2 = i
            arr[char_pos1], arr[char_pos2] = arr[char_pos2], arr[char_pos1]
            arr[char_pos1 + 1:] = reversed(arr[char_pos1 + 1:])
            bigger_word = ''.join(arr)

    return bigger_word


if __name__ == '__main__':
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = bigger_is_greater(w)
        print(result)
