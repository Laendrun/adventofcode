numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

def get_pos(line):
	nums = []
	for i in range(len(numbers)):
		positions = [(pos, i + 1) for pos in range(len(line)) if line.startswith(numbers[i], pos)]
		nums.extend(positions)
	for i in range(len(digits)):
		positions = [(pos, i + 1) for pos in range(len(line)) if line.startswith(digits[i], pos)]
		nums.extend(positions)
	nums.sort()
	return ((min(nums, key=lambda x: x[0]), max(nums, key=lambda x: x[0])))

def get_num(line):
	pos = get_pos(line)
	print(pos)
	return (str(pos[0][1])+str(pos[1][1]))

sum = 0
with open("./input.txt") as f:
	for line in f:
		sum += int(get_num(line))

print(sum)