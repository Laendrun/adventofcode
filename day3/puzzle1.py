import re

with open("./input.txt", "r") as f:
	inp = f.read().split('\n')

valid = []
for i, row in enumerate(inp):
	matches = re.finditer(r"\d+", row)
	length = len(row)
	for match in matches:
		start_i = match.start()
		end_i = match.end()
		number = match.group()
		ind = [start_i, end_i]
		for j in range(int(ind[0]) - 1, int(ind[1]) + 1):
			# previous row
			if i > 0 and j < length:
				if inp[i - 1][j] != '.' and not inp[i - 1][j].isnumeric():
					valid.append(int(number))
					break
			# current row
			if i > 0 and j < length:
				if inp[i][j] != '.' and not inp[i][j].isnumeric():
					valid.append(int(number))
					break
			# next row
			if i < length - 1 and j < length:
				if inp[i + 1][j] != '.' and not inp[i + 1][j].isnumeric():
					valid.append(int(number))
					break
print(sum(valid))