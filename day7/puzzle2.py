with open("./input.txt", "r") as f:
	lines = f.read().split("\n")
	input_data = [line.split(" ") for line in lines]
	input_data = [[line[0], int(line[1])] for line in input_data if len(line) == 2]

# Updated card_map to consider the new rule
card_map = {
	'J': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'T': 10,
	'Q': 11,
	'K': 12,
	'A': 13
}

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

for line in input_data:
	chars = {}
	for char in line[0]:
		chars[char] = chars.get(char, 0) + 1

	keys = list(chars.keys())
	values = list(chars.values())

	if chars.get("J", 0) < 5:
		max_count = max(chars.values())
		max_key = max(chars, key=lambda k: chars[k] if k != "J" else 0)
		chars[max_key] += chars.get("J", 0)
		chars.pop("J", None)
		keys = list(chars.keys())
		values = list(chars.values())

	if len(keys) == 1:
		five_of_a_kind.append(line)
	elif len(keys) == 2:
		if 4 in values:
			four_of_a_kind.append(line)
		else:
			full_house.append(line)
	elif len(keys) == 3:
		if 3 in values:
			three_of_a_kind.append(line)
		else:
			two_pairs.append(line)
	elif len(keys) == 4:
		one_pair.append(line)
	else:
		high_card.append(line)

def sort_cards(card):
	return (
		card_map[card[0][0]],
		card_map[card[0][1]],
		card_map[card[0][2]],
		card_map[card[0][3]],
		card_map[card[0][4]]
	)

five_of_a_kind.sort(key=sort_cards)
four_of_a_kind.sort(key=sort_cards)
full_house.sort(key=sort_cards)
three_of_a_kind.sort(key=sort_cards)
two_pairs.sort(key=sort_cards)
one_pair.sort(key=sort_cards)
high_card.sort(key=sort_cards)

result_array = high_card + one_pair + two_pairs + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
result_sum = sum(x[1] * (i + 1) for i, x in enumerate(result_array))
print(result_sum)