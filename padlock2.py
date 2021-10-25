#puzzle 2

from itertools import product

#second and fifth condition are same with different numbers, so these two condition are taken
def second_fifth_condition(candidate, condition):
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (candidate.index(common_elements[0]) != condition.index(common_elements[0]) )

#for the candidate with one right digit in right place
def first_condition(candidate):
    condition = (6, 8, 2)
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (candidate.index(common_elements[0]) == condition.index(common_elements[0]) )

#for the candidate with two right digit in wrong place
def third_condition(candidate):
    condition = (2, 0, 6)
    common_elements = [digit for digit in candidate if digit in condition]
    if len(common_elements) != 2:
        return False
    for digit in common_elements:
        if candidate.index(digit) == condition.index(digit):
            return False
    return True

#when all digit of condition are wrong there wont be any common elements
def fourth_condition(candidate):
    condition = (7 ,3 ,8)
    common_elements = [digit for digit in candidate if digit in condition]
    return len(common_elements) == 0

#product of itertools gives cartesain product of range(10) i.e (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) with three element in set
def find_code():
    for candidate in product(range(10), repeat=3):
        if(second_fifth_condition(candidate, (6 ,1, 4)) and first_condition(candidate) and third_condition(candidate) and fourth_condition(candidate) and second_fifth_condition(candidate, (3, 8, 0))):
            return "".join(map(str, candidate))
    return "No solution found."


print(find_code())