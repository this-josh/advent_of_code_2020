with open("./inputs/day_8.txt", "r") as f:
    input_data = f.readlines()

input_data = [line.strip() for line in input_data]

cont = True
lines_done = []
index = 0
acc_val = 0
while cont is True:
    if index in lines_done:
        print(acc_val)
        break
    this_line = input_data[index].split(" ")
    method = this_line[0]
    value = int(this_line[1])

    if method == "acc":
        acc_val += value
    if method == "jmp":
        index += value
    else:
        index += 1

    lines_done.append(index)
    