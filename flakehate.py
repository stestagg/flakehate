import sys


def check(source):
	for line in source.splitlines():

		if set(str(len(line.strip()))) != set(['6']):
			raise ValueError("Line lengths must be 6, 66, 666, or 6666 chars long")

if __name__ == "__main__":
	source = sys.stdin.read()
	check(source)