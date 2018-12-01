# URL: https://adventofcode.com/2018/day/1

frequency_variations = []

with open('input.txt') as input_file:
    for line in input_file:
        frequency_variations.append(int(line.rstrip('\n')))

print(sum(frequency_variations))
