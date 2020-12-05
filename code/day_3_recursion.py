with open("./inputs/day_3_a.txt", "r") as f:
    input_data = f.readlines()

# remove new line
input_data = [line.strip() for line in input_data]
width = len(input_data[0])

right = 3
down = 1
def count_trees(input_data, right, down):
    trees = 0
    no_trees = 0

    for move in range(1, len(input_data)):
        x_coord = (move*right) % width
        y_coord = (move*down)
        if y_coord>len(input_data):
            print(down)
            break
        char = input_data[y_coord][x_coord]
        if char =='#':
            trees+=1
        else:
            no_trees+=1
    
    return trees


pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for pair in pairs:
    results.append(count_trees(input_data, pair[0], pair[1]))

import numpy as np
# a = np.prod(results)
trees = count_trees(input_data, right, down)
print(trees)
"""
wrong answers:
82*241*72*68*24 =2322114048 too big
"""
