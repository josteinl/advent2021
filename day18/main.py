from typing import List, Optional


def explode(numbers, level=1):
    exploded = False
    [left, right] = numbers

    if (
        level >= 4
        and isinstance(left, list)
        and isinstance(left[0], int)
        and isinstance(left[1], int)
    ):
        return [0, right + left[1]], True
    elif (
        level >= 4
        and isinstance(right, list)
        and isinstance(right[0], int)
        and isinstance(right[1], int)
    ):
        return [right[0] + left, 0], True

    if isinstance(left, list):
        left, exploded = explode(left, level + 1)
    if isinstance(right, list):
        right, exploded = explode(right, level + 1)

    return [left, right], exploded


def split(numbers):
    return numbers


def numbers_depth(numbers):
    if isinstance(numbers[0], int):
        depth_left = 0
    else:
        depth_left = numbers_depth(numbers[0]) + 1

    if isinstance(numbers[1], int):
        depth_right = 0
    else:
        depth_right = numbers_depth(numbers[1]) + 1

    return max(depth_left, depth_right)


def reduce_numbers(numbers):
    """reduce a snailfish number"""

    # find if we should do
    last_numbers = None
    while True:
        depth = numbers_depth(numbers)
        print(f"{depth=}")
        if depth > 4:
            f = explode
        else:
            f = split
        # explode if there are four/five nested numbers
        # otherwise, split

        numbers = f(numbers)
        if numbers == last_numbers:
            break
        last_numbers = numbers

    return numbers


def add_numbers(numbers, row):
    numbers = [numbers, row]
    numbers = reduce_numbers(numbers)
    return numbers


def main_1():
    with open("test_data.txt") as f:
        numbers = None
        for row in f.readlines():
            row = eval(row)
            if not numbers:
                numbers = row
            else:
                numbers = add_numbers(numbers, row)
            print(f"{numbers}")

        print(f"{numbers}")


if __name__ == "__main__":
    main_1()
