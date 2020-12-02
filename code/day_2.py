# There's a lot of parsing involved in the one

with open("./inputs/day_2.txt", "r") as f:
    input_data = f.readlines()

input_data = [line.replace("\n", "").split(": ") for line in input_data]
print(f"There are {len(input_data)} passwords to check")


def part_one(input_data):
    num_valid = 0
    num_invalid = 0
    for line in input_data:
        char = line[0][-1]
        num_char = line[1].count(char)

        num_range = line[0].split("-")
        min_number = int(num_range[0])
        max_number = int(num_range[1].split(" ")[0])
        if num_char in range(min_number, max_number + 1):
            num_valid += 1
        else:
            num_invalid += 1

    return num_valid, num_invalid


num_valid, num_invalid = part_one(input_data)
print(f"{num_valid=}")
print(f"{num_invalid=}")


def part_two(input_data):
    num_valid = 0
    num_invalid = 0
    for line in input_data:
        char = line[0][-1]
        string = line[1]
        num_range = line[0].split("-")
        first_char = int(num_range[0])
        second_char = int(num_range[1].split(" ")[0])
        # Note it needs XOR
        if (string[first_char - 1] == char) ^ (string[second_char - 1] == char):
            num_valid += 1
        else:
            num_invalid += 1


num_valid, num_invalid = part_two(input_data)

print(f"{num_valid=}")
print(f"{num_invalid=}")
