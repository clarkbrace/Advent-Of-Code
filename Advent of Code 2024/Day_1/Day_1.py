from collections import Counter

def part_one() -> int:
    with open("Day_1.txt", "r") as File:
        left_list = list()
        right_list = list()

        for line in File:

            list_row = line.rstrip().split("   ")

            print(list_row)
            left_list.append(int(list_row[0]))
            right_list.append(int(list_row[1]))

        left_list.sort()
        right_list.sort()

        smallest_sum = 0
        for index in range(len(left_list)):
            smallest_sum += abs(left_list[index] - right_list[index])
        return smallest_sum


def part_two() -> int:
    with open("Day_1.txt", "r") as File:

        left_list = list()
        right_list = list()

        for line in File:

            (left_id, right_id) = line.strip().split("   ")

            left_list.append(int(left_id))
            right_list.append(int(right_id))

        right_list_frequency = Counter(right_list)
        # print(right_list_frequency)

        left_column_frequency_multiplied = 0
        for id_number in left_list:
            # print(id_number * right_list_frequency[id_number])
            left_column_frequency_multiplied += (id_number * right_list_frequency[id_number])

        return left_column_frequency_multiplied


print(part_two())