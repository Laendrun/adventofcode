import re

with open("./input.txt", "r") as f:
	inp = f.read().split('\n')

points = 0
for line in inp:
	my_nums = line.split(':')[1].split('|')[0].split()
	win_nums = line.split(':')[1].split('|')[1].split()
	found = 0
	game_points = 0
	for n in my_nums:
		if n in win_nums and found == 0:
			found += 1
			game_points += 1
		else:
			if n in win_nums and found > 0:
				found += 1
				game_points *= 2
	points += game_points

print(points)