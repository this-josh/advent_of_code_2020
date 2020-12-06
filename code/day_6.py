with open("./inputs/day_6.txt", "r") as f:
    input_data = f.readlines()

input_data = [line.strip() for line in input_data]
input_data.append("")  #  don't miss the last line

def common_values(people):
    from functools import reduce
    return list(reduce(lambda i, j: i & j, (set(x) for x in people))) 


def part_one(input_data):
    # Divide into groups
    # len(set(group))
    this_group = ""
    number_of_yes = 0
    for line in input_data:
        if line == "":
            this_group = set(this_group)
            number_of_yes += len(this_group)

            this_group = ""
            continue
        this_group += line
    return number_of_yes


def part_two(input_data):
    people_in_group = []
    number_of_all_yes = 0
    for person in input_data:
        if person == '':
            number_of_all_yes +=len(common_values(people_in_group))
            people_in_group = []
            continue
        people_in_group.append(set(person))

    return number_of_all_yes


one = part_one(input_data)
two = part_two(input_data)
print(one)
print(two)