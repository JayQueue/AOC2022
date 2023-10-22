# For example, suppose you were given the following strategy guide:
#
# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:
# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8
# (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
# Rock:     A - X = 1
# Paper:    B - Y = 2
# Scissors: C - Z = 3

with open("2_input.txt") as f:
    for line in f:
        tegenstander, ik = line.strip().split(" ")
        print(f"Tegenstander kiest {tegenstander} en ik kies {ik}")
        # Wins: Rock A vs Scissors Y
        #       Paper B vs Rock X
        #       Scissors C vs Rock Y
        if (tegenstander == "A" and ik == "Z") or (tegenstander == "B" and ik == "X") or (tegenstander == "C" and ik == "Y"):
            print(f"{tegenstander} vs {ik}")
        #elif tegenstander == "A" and ik == "Y":
        #    print("Rock vs Paper")
        #elif tegenstander == "A" and ik == "Z":
        #    print("Rock vs Scissors")
        elif tegenstander == "B" and ik == "X":
            print("Paper vs Rock")
        elif tegenstander == "B" and ik == "Y":
            print("Paper vs Paper")
        elif tegenstander == "B" and ik == "Z":
            print("Paper vs Scissors")
        elif tegenstander == "C" and ik == "X":
            print("Scissors vs Rock")
        elif tegenstander == "C" and ik == "Y":
            print("Scissors vs Paper")
        elif tegenstander == "C" and ik == "Z":
            print("Scissors vs Scissors")