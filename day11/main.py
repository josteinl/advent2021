from typing import List, Optional
from pprint import pprint


def increase_energy(octos):
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            octos[y][x] += 1
    return octos


def increase_around(octos, x, y):
    """Increase all around with one"""
    for _x in range(x - 1, x + 2):
        for _y in range(y - 1, y + 2):
            if (
                _x >= 0
                and _x < len(octos[1])
                and _y >= 0
                and _y < len(octos)
                and (_x != x or _y != y)
            ):
                octos[_y][_x] += 1
    return octos


def flash(octos):
    flashers = set()
    while True:
        old_flashers = len(flashers)
        for y in range(len(octos)):
            for x in range(len(octos[0])):
                if octos[y][x] > 9 and (x, y) not in flashers:
                    flashers.add((x, y))
                    octos = increase_around(octos, x, y)

        new_flashers = len(flashers) - old_flashers
        if new_flashers <= 0:
            break

    return octos, flashers


def reset_flashers(octos, flashers):
    for x, y in flashers:
        octos[y][x] = 0
    return octos


def main_1():
    with open("data.txt") as f:
        octos = []
        for row in f.readlines():
            octos.append([int(digit) for digit in row.strip()])

    print(f"Start:")
    pprint(octos)

    all_flash_steps = []
    number_of_flashes = 0
    for step in range(10000):
        # 1 increase all octos
        octos = increase_energy(octos)
        # 2 flash
        octos, flashers = flash(octos)
        if len(flashers) == len(octos) * len(octos[0]):
            # all falshes
            all_flash_steps.append(step)
        number_of_flashes += len(flashers)
        # 3 Set flashers to 0
        octos = reset_flashers(octos, flashers)

        print(f"After {step=}:")
        # pprint(octos)
    print(f"{number_of_flashes=}")
    print(f"{all_flash_steps=}")  # step += 1 due to 0 indexing


def main_2():
    """Try to optimize by grouping all fish that has the same timer"""
    with open("data.txt") as f:
        start_numbers = [int(number) for number in f.readline().split(",")]

        print(f"{result=}")


if __name__ == "__main__":
    main_1()
    # main_2()
