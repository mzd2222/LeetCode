from typing import List

def plusOne(digits: List[int]):

    digits[len(digits)-1] += 1

    for i in range(len(digits)-1, -1, -1):

        if digits[i] == 10:
            digits[i] = 0

            if i-1 < 0:
                digits.insert(0, 1)
            else:
                digits[i-1] += 1

    return digits


print(plusOne([9,9,9,9]))

