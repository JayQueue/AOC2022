teller = 0
som = 0
with open("3_input_full.txt") as f:
    for line in f:
        middle = len(line)//2
        for letter in set(line.strip()[0:middle]).intersection(line.strip()[middle:]):
            if letter.islower():
                som += ord(letter) - 96
            else:
                som += (ord(letter) - 64) + 26
    # Part 1
    print(f"Sum: {som}")

    # Part 2
    ...

