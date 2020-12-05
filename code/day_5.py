with open("./inputs/day_5.txt", "r") as f:
    input_data = f.readlines()

input_data = [line.strip() for line in input_data]


def find_row(full_string):
    row_info = full_string[:7]
    rows = list(range(128))

    for char in row_info:
        if char == "F":
            rows = rows[: int(len(rows) / 2)]
        elif char == "B":
            rows = rows[int(len(rows) / 2) :]
        else:
            print(char)
            raise
    return rows[0]


def find_col(full_string):
    col_info = full_string[7:]
    cols = list(range(8))

    for char in col_info:
        if char == "L":
            cols = cols[: int(len(cols) / 2)]
        elif char == "R":
            cols = cols[int(len(cols) / 2) :]
        else:
            print(char)
            raise
    return cols[0]


def get_seat_id(row_num, col_num):
    return (row_num * 8) + col_num


all_seat_ids = []
for seat in input_data:
    row_num = find_row(seat)
    col_num = find_col(seat)
    seat_id = get_seat_id(row_num, col_num)
    all_seat_ids.append(seat_id)


print(max(all_seat_ids))

# part 2
all_seat_ids.sort()
for index in range(1, len(all_seat_ids)):
    diff = all_seat_ids[index] - all_seat_ids[index - 1]
    if diff == 2:
        print(all_seat_ids[index] - 1)
