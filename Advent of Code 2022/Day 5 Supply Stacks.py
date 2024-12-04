from itertools import islice

stacks = [[] for i in range(9)]
with open("Aux files/input 5 Supply Stacks.txt") as file:
    # Grab all the input lines
    inputLines = list(islice(file, 8))
    # Go over all lines in reverse
    for crates in reversed(inputLines):
        stacks[0].append(crates[1])

        if
        stacks[1].append(crates[5])
        stacks[2].append(crates[9])
        stacks[3].append(crates[13])
        stacks[4].append(crates[17])
        stacks[5].append(crates[21])
        stacks[6].append(crates[25])
        stacks[7].append(crates[29])
        stacks[8].append(crates[33])

    # print(stacks)
    print("This:", stacks[1][4])
    for stack in stacks:



print(stacks)


