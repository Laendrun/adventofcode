def winning_count(race: tuple[int, int]) -> int:
	count = 0
	time = race[0]
	d = race[1]
	for hold in range(1, time):
		runtime = time - hold
		speed = hold
		D = speed * runtime
		if D > d:
			count += 1

	return count

def get_result(data: list[tuple[int, int]]) -> int:
	wc: list[int] = []
	for i in range(len(data)):
		wc.append(winning_count(data[i]))
	print(wc)
	x = 1
	for i in range(len(wc)):
		x *= wc[i]
	return x

def main():
	with open("./input.txt", "r") as f:
		time_data: list[str] = f.readline().strip().split(':')[1].split()
		dist_data: list[str] = f.readline().strip().split(':')[1].split()
	print(winning_count((int(''.join(time_data)), int(''.join(dist_data)))))


if __name__ == "__main__":
	main()