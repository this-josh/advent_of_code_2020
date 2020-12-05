import re


required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])


def byr_check(value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    value = int(value)
    return (value >= 1920) & (value <= 2002)


def iyr_check(value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    value = int(value)

    return (value >= 2010) & (value <= 2020)


def eyr_check(value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    value = int(value)

    return (value >= 2020) & (value <= 2030)


def hgt_check(value):

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.

    suffix = value[-2:]
    try:
        number = int(value[:-2])
    except ValueError:
        return False

    if suffix == "cm":
        return (number >= 150) & (number <= 193)
    elif suffix == "in":
        return (number >= 59) & (number <= 76)
    else:
        return False

def hcl_check(value):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    import re

    return re.search(r"^#[0-9a-f]{6}$", value)


def ecl_check(value):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in valid_colours


def pid_check(value):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    import re

    return re.search(r"^[0-9]{9}$", value)


def check_all(this_passport):
    byr = byr_check(this_passport["byr"])
    iyr = iyr_check(this_passport["iyr"])
    eyr = eyr_check(this_passport["eyr"])
    hgt = hgt_check(this_passport["hgt"])
    hcl = hcl_check(this_passport["hcl"])
    ecl = ecl_check(this_passport["ecl"])
    pid = pid_check(this_passport["pid"])
    print(f'{byr=}, {iyr=}, {eyr=}, {hgt=}, {hcl=}, {ecl=}, {pid=}')
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])


# ignore cid

with open("./inputs/day_4.txt", "r") as f:
    input_data = f.readlines()

input_data = [line.strip() for line in input_data]

okay_passports = 0
bad_passports = []
this_passport = {}
line_number = 1
for line in input_data:
    line_number += 1
    if line == "":
        missing_fields = required_fields - set(this_passport.keys())
        if len(missing_fields) == 0 and check_all(this_passport) is True:
            okay_passports += 1
        else:
            bad_passports.append(missing_fields)
        this_passport = {}
        continue
    this_line_cats = line.split(" ")
    for cat in this_line_cats:
        values = cat.split(":")
        this_passport[values[0]] = values[1]

print(okay_passports)