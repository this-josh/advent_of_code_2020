import numpy as np

inputs = np.loadtxt("inputs/day_1.txt")


def first_task(inputs):
    """find the two entries that sum to 2020, multiply them"""
    # let's start ugly
    for val1 in inputs:
        for val2 in inputs:
            if val1 + val2 == 2020:
                print(val1, val2, val1 * val2)
                return


def second_task(inputs):
    """find the three entries that sum to 2020, multiply them"""
    for val1 in inputs:
        for val2 in inputs:
            for val3 in inputs:
                if val1 + val2 + val3 == 2020:
                    print(val1, val2, val3, val1 * val2 * val3)
                    return


def in_one(inputs, num_to_sum):
    """find the three entries that sum to 2020, multiply them"""
    import itertools

    for values in itertools.product(*[inputs] * num_to_sum):
        if sum(values) == 2020:
            return np.prod(values)


# These could be refactored into one method
first_task(inputs)
second_task(inputs)

# In one method
print(in_one(inputs, 2))
print(in_one(inputs, 3))
