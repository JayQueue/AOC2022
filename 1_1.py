# Advent of Code
# Learning Python
# Day 1: https://adventofcode.com/2022/day/1
# Day 1 input; https://adventofcode.com/2022/day/1/input
#
# Part 1: Highest amount of calories
# Part 2: Sum of top 3 highest amount of calories

totals = []
total = 0

# Read file
with open("1_input_full.txt") as f:
    print("Start")
    for line in f:
        print(line.strip())
        if line.strip() != "":
            total = total + int(line.strip())
        else:
            totals.append(total)
            total = 0
print(totals)
# Part 1
print(f"Max: {max(totals)}")
# Part 2
print(f"Sum Top 3: {sum(sorted(totals, reverse=True)[:3])}")
