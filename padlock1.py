#puzzle 1

from itertools import product

#first and fifth condition are same with different number, so these two condition are taken
def first_fifth_condition(candidate, condition):
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (candidate.index(common_elements[0]) != condition.index(common_elements[0]) )

#for the candidate with one right digit in right place
def second_condition(candidate):
    condition = (1, 8, 9)
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (candidate.index(common_elements[0]) == condition.index(common_elements[0]) )

#for the candidate with two right digit in wrong place
def third_condition(candidate):
    condition = (9, 6, 4)
    common_elements = [digit for digit in candidate if digit in condition]
    if len(common_elements) != 2:
        return False
    for digit in common_elements:
        if candidate.index(digit) == condition.index(digit):
            return False
    return True

def fourth_condition(candidate):
    condition = (5 ,2 ,3)
    common_elements = [digit for digit in candidate if digit in condition]
    return len(common_elements) == 0

#product of itertools gives cartesain product of range(10) i.e (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) with three element in set
def find_code():
    for candidate in product(range(10), repeat=3):
        if(first_fifth_condition(candidate, (1 ,4, 7)) and second_condition(candidate) and third_condition(candidate) and fourth_condition(candidate) and first_fifth_condition(candidate, (2, 8, 6))):
            return "".join(map(str, candidate))
    return "No solution found."


print(find_code())
    