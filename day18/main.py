from typing import List, Optional


def explode(numbers, level=1):
    exploded_left = [0, 0]
    exploded_right = [0, 0]
    [left, right] = numbers

    if level > 4 and isinstance(left, int) and isinstance(right, int):
        return 0, numbers

    if isinstance(left, list):
        left, exploded_left = explode(left, level + 1)
    if isinstance(right, list):
        if exploded_left[1]:
            right[0] += exploded_left[1]
            exploded_left[1] = 0
        elif exploded_left == [0, 0]:
            right, exploded_right = explode(right, level + 1)

    rest = [
        exploded_left[0] + exploded_right[0],
        exploded_left[1] + exploded_right[1],
    ]

    if isinstance(numbers[0], int) and rest[0]:
        left = left + rest[0]
        rest[0] = 0
    if isinstance(numbers[1], int) and rest[1]:
        right = right + rest[1]
        rest[1] = 0

    return [left, right], rest


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
