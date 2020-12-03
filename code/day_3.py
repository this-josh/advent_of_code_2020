with open("./inputs/day_3.txt", "r") as f:
    input_data = f.readlines()

# remove new line
input_data = [line.replace("\n", "") for line in input_data]


def iter_time(input_data, right, down):
    num_moves = int(len(input_data) / down)
    max_right = num_moves * right
    width = len(input_data[0])
    times_repeated = int((max_right / width) + 1)

    whole_array = [line * times_repeated for line in input_data]

    # create array of places you'd visit
    coords = []
    trees = 0
    no_trees = 0
    i = 1
    for move in range(1, num_moves ):
        i += 1
        if i == 160:
            print("g")
        # move+=1
        x = right * move
        y = down * move
        if whole_array[y][x] == "#":
            trees += 1
        else:
            no_trees += 1
    
    assert trees+no_trees == (len(whole_array)-1)

    return trees+1


pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for pair in pairs:
    results.append(iter_time(input_data, *pair))

import numpy as np
# 2005104832 too low

print(np.product(results))

