from typing import List, Union, Tuple


def add_number_to_last(numbers: str, first: int):
    found_digit = False
    for i, char in enumerate(numbers[::-1]):
        if char.isdigit():
            found_digit = True
            end_digit = i
        elif found_digit:
            start_digit = i
            number = int(numbers[-start_digit:-end_digit])
            new_number = number + first

            return numbers[:-start_digit] + str(new_number) + numbers[-end_digit:]

    return numbers


def add_number_to_first(numbers: str, second: int):
    number = 0
    factor = 1
    found_digit = False
    for i, char in enumerate(numbers):
        if char.isdigit():
            found_digit = True
            start_digit = i
            number += int(char) * factor
            factor *= 10
        elif found_digit:
            end_digit = i
            new_number = number + second
            return numbers[:start_digit] + str(new_number) + numbers[end_digit:]

    return numbers


def explode(numbers: str):

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
                print("not a pair")
                continue
            first = int(numbers[i + 1 : comma + 1])
            second = int(numbers[comma + 2 : end + 1])

            return (
                add_number_to_last(numbers[:i], first)
                + "0"
                + add_number_to_first(numbers[end + 2 :], second)
            )


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


def numbers_depth(numbers):
    max_depth = 0
    depth = 0
    for char in numbers:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        max_depth = max(max_depth, depth)

    return max_depth


def reduce_numbers(numbers):
    """reduce a snailfish number"""

    # find if we should do
    last_numbers = []
    while True:
        depth = numbers_depth(numbers)
        # print(f"{depth=}")
        if depth >= 4:
            print(f"explode()")
            numbers = explode(numbers)
        else:
            print(f"split()")
            numbers, _ = split(numbers)

        print(
            f"{numbers=} len:{len(repr(numbers))} diff={-len(repr(last_numbers)) + len(repr(numbers))}"
        )
        if numbers == last_numbers:
            break
        last_numbers = numbers

    return numbers


def add_numbers(numbers, row):
    numbers = f"[{numbers}{row}]"
    print(f"Add numbers:")
    print(f"{numbers=}")
    numbers = reduce_numbers(numbers)
    return numbers


def main_1():
    with open("test_data.txt") as f:
        numbers = None
        for row in f.readlines():
            row = row.strip()
            if not numbers:
                numbers = row
                print(f"Start :{numbers}")
            else:
                print(f"Add   :{row}")
                numbers = add_numbers(numbers, row)
                print(f"Result:{numbers}")

        print(f"{numbers}")


if __name__ == "__main__":
    main_1()
