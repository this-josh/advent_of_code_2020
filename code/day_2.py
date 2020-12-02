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
