import re

with open("./input.txt", "r") as f:
	inp = f.read().split('\n')

# will store the positions of all asterisk (i, j)
# i => col index
# j => row index
star_positions = []
for j, row in enumerate(inp):
	matches = re.finditer(r"\*", row)
	for match in matches:
		i = match.start()
		star_positions.append((i, j))

# will store the positions of all numbers (start_i, end_i, j, number)
# start_i => column starting the number
# end_i => column finishing the number
# j => row index
# number => the actual number
number_positions = []
for j, row in enumerate(inp):
	matches = re.finditer(r"\d+", row)
	for match in matches:
		start_i = match.start()
		end_i = match.end() - 1
		number = int(match.group())
		number_positions.append((start_i, end_i, j, number))

total = 0
for star_i, star_j in star_positions:
	adjacent = []
	for start_i, end_i, j, number in number_positions:
		if ((start_i >= star_i - 1 and start_i <= star_i + 1) or (end_i >= star_i - 1 and end_i <= star_i + 1)):
			if ((j >= star_j - 1 and j <= star_j + 1)):
				adjacent.append(number)
	if (len(adjacent) == 2):
		total += adjacent[0] * adjacent[1]
		print(total)

print(total)
