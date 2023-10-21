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
    # Read first line
    line = f.readline()
    # Repeat until EOF
    while line:
        # If calories are grouped together add them
        # to total and if there's another block, reset total
        # add to totals list
        if line.strip() != "":
            total = total + int(line.strip())
        else:
            total = 0
        totals.append(total)
        # Read next line
        line = f.readline()
    # Part 1
    # Print max of the totals list
    print(f"Max: {max(totals)}")

    # Part 2
    # Print sum of a reversed sorted list where I got the first 3 items
    print(f"Sum Top 3: {sum(sorted(totals, reverse=True)[:3])}")
