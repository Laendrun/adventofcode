import re

def get(color, tirage):
	pattern = re.compile(r'(\d+)\s+' + re.escape(color))
	match = pattern.search(tirage)
	if match:
		number = match.group(1)
	else:
		number = 0
	return number

def get_power(line):
	tirages = line.split(';')
	r = g = b = 0
	for tirage in tirages:
		tirage = tirage.strip()
		r2 = int(get('red', tirage))
		g2 = int(get('green', tirage))
		b2 = int(get('blue', tirage))
		r = r2 if r2 > r else r
		g = g2 if g2 > g else g
		b = b2 if b2 > b else b
	power = r * g * b
	return power

with open("./input.txt", "r") as f:
	total = 0
	for line in f:
		total += get_power(line.split(':')[1].strip())
	print(total)