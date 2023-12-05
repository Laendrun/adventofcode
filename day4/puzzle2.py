with open("./input.txt", "r") as f:
	cards = f.read().split('\n')

def get_winning_count(my_nums, win_nums):
	count = 0
	for num in my_nums:
		if num in win_nums:
			count += 1
	return count

# storing one of each card by default
number_of_cards= {}
for x in range(len(cards)):
	number_of_cards[x] = 1

# go through each game
for i, line in enumerate(cards):
	next_card = i + 1
	my_nums = line.split(':')[1].split('|')[0].split()
	winning_nums = line.split(':')[1].split('|')[1].split()
	winning_count = get_winning_count(my_nums, winning_nums)

	for x in range(next_card, next_card + winning_count):
		number_of_cards[x] += number_of_cards[i]

print(sum(number_of_cards.values()))