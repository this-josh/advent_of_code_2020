# I downloaded day 3's input wrong. Going to check the difference here
with open("./inputs/day_3_a.txt", "r") as f:
    input_a = f.readlines()

# remove new line
input_a = [line.strip() for line in input_a]

with open("./inputs/day_3_a.txt", "r") as f:
    input_original = f.readlines()

# remove new line
input_original = [line.strip() for line in input_original]

for index in range(len(input_a)):
    if input_a[index]!=input_original[index]:
        print('gr')