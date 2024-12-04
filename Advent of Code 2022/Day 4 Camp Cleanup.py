# Part 1
import re
overlap_count = 0
with open("Aux files/input 4 camp cleanup") as file:
    for line in file:
        line = line.strip()  # Remove extra white space
        line = re.split('-|,', line)  # Deliminated by two values

        if int(line[0]) < int(line[2]):
            if int(line[1]) >= int(line[3]):
                overlap_count += 1
        elif int(line[2]) < int(line[0]):
            if int(line[3]) >= int(line[1]):
                overlap_count += 1
        elif int(line[0]) == int(line[2]) or int(line[1]) == int(line[3]):
            overlap_count += 1


print(overlap_count)

# other answer! : 595
overlap_count = 0  # Reset overlap count
with open("Aux files/input 4 camp cleanup") as file:
    for line in file:
        line = line.strip()  # Remove extra white space
        line = re.split('-|,', line)  # Deliminated by two values

        if int(line[2]) <= int(line[0]) <= int(line[3]):
            overlap_count += 1
        elif int(line[2]) <= int(line[1]) <= int(line[3]):
            overlap_count += 1
        elif int(line[0]) <= int(line[2]) <= int(line[1]):
            overlap_count += 1
        elif int(line[0]) <= int(line[3]) <= int(line[1]):
            overlap_count += 1

print(overlap_count)
