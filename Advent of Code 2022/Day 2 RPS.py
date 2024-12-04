# Read in file
total_score = 0

with open("Aux files/input 2 RPS.txt") as file:
    for line in file:
        shape_selected = line[2]
        shape_opponent_selected = line[0]

        if shape_selected == "X":  # Selected Rock
            total_score += 1

            # Outcome
            if shape_opponent_selected == "A":  # Opponent
                total_score += 3
            elif shape_opponent_selected == "C":  # Opponent
                total_score += 6

        elif shape_selected == "Y":  # Selected Paper
            total_score += 2

            # Outcome
            if shape_opponent_selected == "B":  # Opponent
                total_score += 3
            elif shape_opponent_selected == "A":  # Opponent
                total_score += 6

        elif shape_selected == "Z":  # Selected Scissors
            total_score += 3

            # Outcome
            if shape_opponent_selected == "C":  # Opponent
                total_score += 3
            elif shape_opponent_selected == "B":  # Opponent
                total_score += 6

        else:
            print("Error occurred. Unknown shape played:", shape_selected)
file.close()

print(total_score)

total_score = 0
# Part 2
with open("Aux files/input 2 RPS.txt") as file:
    for line in file:
        shape_selected = line[2]
        shape_opponent_selected = line[0]
        if shape_selected == "X":  # You need to loose
            # Outcome
            if shape_opponent_selected == "A":  # Opponent plays rock
                total_score += 3
            elif shape_opponent_selected == "B":  # Opponent plays paper
                total_score += 1
            elif shape_opponent_selected == "C":  # Opponent plays scissors
                total_score += 2

        elif shape_selected == "Y":  # You need to draw
            total_score += 3
            # Outcome
            if shape_opponent_selected == "A":  # Opponent plays rock
                total_score += 1
            elif shape_opponent_selected == "B":  # Opponent plays paper
                total_score += 2
            elif shape_opponent_selected == "C":  # Opponent plays scissors
                total_score += 3

        elif shape_selected == "Z":  # You need to win
            total_score += 6
            # Outcome
            if shape_opponent_selected == "A":  # Opponent plays rock
                total_score += 2
            elif shape_opponent_selected == "B":  # Opponent plays paper
                total_score += 3
            elif shape_opponent_selected == "C":  # Opponent plays scissors
                total_score += 1
file.close()

print(total_score)
