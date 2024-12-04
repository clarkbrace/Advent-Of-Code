from itertools import islice

# Part 1
common_items = []
with open("Aux files/input 3 rucksack.txt") as file:
    for line in file:
        line = line.strip()
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]

        common = []
        for item in comp1:
            if item in comp2 and item not in common:
                common.append(item)
        common_items += common
file.close()

print(common_items)
# Process to find priority sum
priority_sum = 0

for item in common_items:
    val = ord(item)
    if val >= 97:
        priority_sum += val - 96
    else:
        priority_sum += val - 38

print(priority_sum)

# Part 2
# get file
# Badge Items
badge_items = []
with open("Aux files/input 3 rucksack.txt") as file:
    while True:
        # Group all by 3
        group = list(islice(file, 3))

        # End reading the file has completely been read
        if not group:
            break
        # remove all new line characters
        group = list(map(str.strip, group))

        for item in group[0]:
            if item in group[1] and item in group[2]:
                badge_items.append(item)
                break

print(badge_items)

priority_sum = 0

for item in badge_items:
    val = ord(item)
    if val >= 97:
        priority_sum += val - 96
    else:
        priority_sum += val - 38

print(priority_sum)






