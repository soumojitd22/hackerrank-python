"""
designer-pdf-viewer
"""


def designerPdfViewer(h, word):
    highest_word = h[ord(word[0]) - ord('a')]
    for w in word:
        if h[ord(w) - ord('a')] > highest_word:
            highest_word = h[ord(w) - ord('a')]

    return highest_word * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(str(result))
