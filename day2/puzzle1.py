# 12 red, 13 green, 14 blue
import re

def get(color, tirage):
	pattern = re.compile(r'(\d+)\s+' + re.escape(color))
	match = pattern.search(tirage)
	if match:
		number = match.group(1)
	else:
		number = 0
	return number

def is_possible(line, id):
	# split on ; to get all inputs
	tirages = line.split(';')
	for tirage in tirages:
		tirage = tirage.strip()
		r = get('red', tirage)
		g = get('green', tirage)
		b = get('blue', tirage)
		if (int(r) > 12 or int(g) > 13 or int(b) > 14):
			return False
	return True
	# print((id, r, g, b))

with open("./input.txt", "r") as f:
	game_id = 0
	total = 0
	for line in f:
		game_id += 1
		if is_possible(line.split(':')[1].strip(), game_id):
			total += game_id
	print(total)