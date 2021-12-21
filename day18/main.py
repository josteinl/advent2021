from typing import List, Union, Tuple


def explode(
    numbers: list, rest_left: int, rest_right: int, done: bool, level: int = 1
) -> Tuple[Union[List, int], int, int, bool]:

    [left, right] = numbers

    if not done and level > 4 and isinstance(left, int) and isinstance(right, int):
        return 0, left, right, True

    if rest_right:
        if isinstance(left, int):
            left += rest_right
            rest_right = 0

    if rest_left:
        if isinstance(right, int):
            right += rest_left
            rest_left = 0

    if isinstance(left, list):
        left, rest_left, rest_right, done = explode(
            left, rest_left, rest_right, done=done, level=level + 1
        )

    # if exploded just now (int now, was list) only pass right rest
    if isinstance(left, int) and isinstance(numbers[0], list):
        right, _, rest_right, done = explode(
            right, 0, rest_right, done=done, level=level + 1
        )
    else:
        if isinstance(right, list):
            right, rest_left, _, done = explode(
                right, rest_left, 0, done=done, level=level + 1
            )

    return [left, right], rest_left, rest_right, done


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
    last_numbers = []
    while True:
        depth = numbers_depth(numbers)
        # print(f"{depth=}")
        if depth >= 4:
            print(f"explode()")
            numbers, _, _ = explode(numbers, rest=[0, 0], done=False)
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
    numbers = [numbers, row]
    print(f"Add numbers:")
    print(f"{numbers=}")
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

        print(f"{numbers}")


if __name__ == "__main__":
    main_1()
