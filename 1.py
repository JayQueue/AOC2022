totals = []
total = 0
with open("1_input_full.txt") as f:
    line = f.readline()
    while line:
        if line.strip() != "":
            total = total + int(line.strip())
        else:
            total = 0
        totals.append(total)
        line = f.readline()
    # Part 1
    print(f"Maximum: {max(totals)}")

    # Part 2
    print(f"Som Top 3: {sum(sorted(totals, reverse=True)[:3])}")
