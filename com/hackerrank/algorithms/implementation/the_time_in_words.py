"""
the-time-in-words
"""


def time_in_words(h, m):
    words = ["o' clock", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes",
             "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes",
             "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes",
             "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes",
             "twenty three minutes", "twenty four minutes", "twenty five minutes", "twenty six minutes",
             "twenty seven minutes", "twenty eight minutes", "twenty nine minutes", "half"]

    if m == 0:
        time = words[h].split()[0] + " " + words[m]
    elif m > 30:
        time = words[(60 - m)] + " to " + words[h + 1].split()[0]
    else:
        time = words[m] + " past " + words[h].split()[0]

    return time


if __name__ == '__main__':
    h = int(input())
    m = int(input())
    result = time_in_words(h, m)
    print(result)
