# Part 1
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
     print(f"Sum part 1: {som}")


# Part 2
som2 = 0
with open("3_input_full.txt") as f2:
    line2 = f2.readlines()
    for i in range(0, len(line2), 3):
        listper3 = [set(p2line.strip('\n')) for p2line in line2[i:i + 3]]
        for letter in set.intersection(*listper3):
            if letter.islower():
                som2 += ord(letter) - 96
            else:
                som2 += (ord(letter) - 64) + 26
    print(f"Sum part 2: {som2}")


