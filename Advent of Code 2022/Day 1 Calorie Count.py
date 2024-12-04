# Read in file
calorie_totals = []
# Open file with the intention to read from it
with open("Aux files/input 1 calorie count.txt", "r") as file:
    currentSum = 0
    for line in file:
        if line != "\n":
            currentSum += int(line)
        else:
            calorie_totals.append(currentSum)
            currentSum = 0
# Part 1
# Find the highest values
highest_calorie_count = 0
for value in calorie_totals:
    if value > highest_calorie_count:
        highest_calorie_count = value

# Print the highest calorie count
print("Highest calorie elf:", highest_calorie_count)


# Part 2
def find_smallest_value(lst):
    smallest = lst[0];
    for num in lst[1:]:
        if smallest > num:
            smallest = num
    return smallest


# Find the total of the top 3 elves
highest_calorie_counts = calorie_totals[0:3]
for value in calorie_totals[3:]:
    smallest_value = find_smallest_value(highest_calorie_counts)
    if value > smallest_value:
        highest_calorie_counts.remove(smallest_value)
        highest_calorie_counts.append(value)

# Print sum of the top three
print("Sum of top three highest calorie elves:", highest_calorie_counts[0] + highest_calorie_counts[1] + highest_calorie_counts[2])
