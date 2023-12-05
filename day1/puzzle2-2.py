import re

def calculate_calibration(lines):
    total = 0

    # Define a dictionary to map spelled-out digits to their numerical values
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for line in lines:
        # Replace spelled-out digits with numerical digits using the dictionary
        line = ''.join([digit_mapping.get(word, word) for word in re.findall(r'\b\w+\b', line)])

        # Extract the first digit using regular expressions
        match_first = re.search(r'\b(\d)\w*\b', line)
        if match_first:
            first_digit = int(match_first.group(1))
        else:
            # Handle the case where no match is found
            first_digit = 0

        # Extract the last digit using regular expressions
        match_last = re.search(r'\b(\d)\w*\b', line[::-1])
        if match_last:
            last_digit = int(match_last.group(1))
        else:
            # Handle the case where no match is found
            last_digit = 0

        # Add the digits to the total
        total += int(str(first_digit) + str(last_digit))

    return total

with open("./input.txt") as f:
    print(calculate_calibration(f.readlines()))