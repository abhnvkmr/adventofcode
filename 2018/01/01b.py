# URL: https://adventofcode.com/2018/day/1

import itertools

frequency_set = {0}
frequency = 0

with open('input.txt') as input_file:
    for line in itertools.cycle(input_file):
        x = int(line.rstrip('\n'))
        frequency = frequency + x
        if frequency in frequency_set:
            print(frequency)
            break
        frequency_set.add(frequency)
