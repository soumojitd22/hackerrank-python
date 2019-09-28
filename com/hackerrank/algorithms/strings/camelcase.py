"""
camelcase
"""


def camelcase(s):
	return sum(map(str.isupper, s)) + 1


if __name__ == "__main__":
	s = input()
	result = camelcase(s)
	print(result)
