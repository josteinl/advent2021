from typing import List, Union, Tuple
from itertools import permutations


def add_number_to_last(numbers: str, first: int):
    found_digit = False
    for i, char in enumerate(numbers[::-1]):
        if char.isdigit():
            if not found_digit:
                end_digit = i
            found_digit = True
        elif found_digit:
            start_digit = i
            number = int(numbers[-start_digit:-end_digit])
            new_number = number + first

            return numbers[:-start_digit] + str(new_number) + numbers[-end_digit:]

    return numbers


def add_number_to_first(numbers: str, second: int):
    found_digit = False
    start_digit = None
    for i, char in enumerate(numbers):
        if char.isdigit():
            if not found_digit:
                start_digit = i
            found_digit = True
        elif found_digit:
            end_digit = i
            number = int(numbers[start_digit:end_digit])
            new_number = number + second
            return numbers[:start_digit] + str(new_number) + numbers[end_digit:]

    return numbers


def explode(numbers: List):
    numbers = repr(numbers).replace(" ", "")

    depth = 0
    for i, char in enumerate(numbers):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1

        if depth > 4 and char == "[":
            # Extract the numbers
            comma = numbers[i + 1 :].index(",") + i
            end = numbers[i + 1 :].index("]") + i
            try:
                next = numbers[i + 1 :].index("[") + i
            except ValueError:
                next = end
            if next < end:
                # Not a pair (but nested)
                # print("not a pair")
                continue
            first = int(numbers[i + 1 : comma + 1])
            second = int(numbers[comma + 2 : end + 1])

            return eval(
                add_number_to_last(numbers[:i], first)
                + "0"
                + add_number_to_first(numbers[end + 2 :], second)
            )
    return numbers


def split(numbers):
    """Only split the left most"""
    [left, right] = numbers
    done = False

    if isinstance(left, int) and left >= 10 and not done:
        left = [left // 2, -(-left // 2)]
        done = True
    elif isinstance(left, list) and not done:
        left, done = split(left)

    if isinstance(right, int) and right >= 10 and not done:
        right = [right // 2, -(-right // 2)]
        done = True
    elif isinstance(right, list) and not done:
        right, done = split(right)

    return [left, right], done


def numbers_depth(numbers: List):
    if isinstance(numbers[0], int):
        depth_left = 1
    else:
        depth_left = numbers_depth(numbers[0]) + 1

    if isinstance(numbers[1], int):
        depth_right = 1
    else:
        depth_right = numbers_depth(numbers[1]) + 1

    return max(depth_left, depth_right)


def calculate_magnitude(number):

    left, right = number
    if isinstance(left, int) and isinstance(right, int):
        return 3 * left + 2 * right

    if isinstance(left, int) and isinstance(right, list):
        return 3 * left + 2 * calculate_magnitude(right)

    if isinstance(left, list) and isinstance(right, int):
        return 3 * calculate_magnitude(left) + 2 * right

    return 3 * calculate_magnitude(left) + 2 * calculate_magnitude(right)


def reduce_numbers(numbers):
    """reduce a snailfish number"""

    # find if we should do
    last_numbers = []
    while True:
        depth = numbers_depth(numbers)
        # print(f"{depth=}")
        if depth > 4:
            # print(f"explode()")
            numbers = explode(numbers)
        else:
            # print(f"split()")
            numbers, _ = split(numbers)

        # print(
        #     f"{numbers=} len:{len(repr(numbers))} diff={-len(repr(last_numbers)) + len(repr(numbers))}"
        # )
        if numbers == last_numbers:
            break
        last_numbers = numbers

    return numbers


def add_numbers(numbers, row):
    numbers = [numbers, row]
    # print(f"Add numbers:")
    # print(f"{numbers=}")
    numbers = reduce_numbers(numbers)
    return numbers


def main_1():
    with open("test_data.txt") as f:
        numbers = None
        for row in f.readlines():
            row = eval(row)
            if not numbers:
                numbers = row
                print(f"Start :{numbers}")
            else:
                print(f"Add   :{row}")
                numbers = add_numbers(numbers, row)
                print(f"Result:{numbers}")

        print(f"{calculate_magnitude(numbers)}")


def main_2():
    with open("data.txt") as f:
        numbers = []
        for row in f.readlines():
            numbers.append(eval(row))

        max_sum = 0
        for number_one, number_two in permutations(numbers, r=2):
            # print(f"{number_one=}")
            max_sum = max(
                calculate_magnitude(add_numbers(number_one, number_two)), max_sum
            )

        print(f"{max_sum=}")


if __name__ == "__main__":
    # main_1()
    main_2()
