

with open("Day_2.txt", "r") as File:

    safe_reports = 0

    for report in File:

        # Split string by spaces
        levels_strings = report.rstrip().split(" ")

        # Convert strings to numbers
        levels_numbers = list()
        for level_string in levels_strings:
            levels_numbers.append(int(level_string))

        # Level length sanity check
        # if len(levels_numbers) < 2:
        #     safe_reports += 1
        #     continue

        # Check to see if levels are increasing or decreasing
        # True is increasing, False is decreasing

        def increasing_check(difference): return 0 < difference < 4
        def decreasing_check(difference): return -4 < difference < 0

        level_rule = increasing_check if levels_numbers[0] < levels_numbers[1] else decreasing_check

        # Puzzle conditions
        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.

        valid_level = True
        used_skip = False

        for level_index in range(len(levels_numbers) - 1):

            current_level_difference = levels_numbers[level_index + 1] - levels_numbers[level_index]

            level_results = level_rule(current_level_difference)

            if not level_rule(current_level_difference):

                if not used_skip:
                    used_skip = True
                    level_index += 1
                else:
                    valid_level = False
                    break

        if valid_level:
            safe_reports += 1

    print(safe_reports)

# if levels_increasing:
#     # Increasing
#     for level_index in range(len(levels_numbers) - 1):
#
#         level_difference = levels_numbers[level_index + 1] - levels_numbers[level_index]
#
#         if level_difference < 1 or level_difference > 3:
#             valid_level = False
#             break
# else:
#     # Decreasing
#     for level_index in range(len(levels_numbers) - 1):
#         level_difference = levels_numbers[level_index + 1] - levels_numbers[level_index]
#
#         if level_difference < -3 or level_difference > -1:
#             valid_level = False
#             break