def get_first(line):
	for i,c in enumerate(line):
		if (line[i].isdigit()):
			return (line[i])

def get_num(line):
	ds = get_first(line)
	dl = get_first(line[::-1])
	return (str(ds)+str(dl))

sum = 0
with open("./input.txt", "r") as f:
	for line in f:
		sum += int(get_num(line))

print(sum)