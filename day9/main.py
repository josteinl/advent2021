from typing import List, Optional
import math


def is_minimum(x, y, floor):
    surrounding_numbers = []
    number = floor[y][x]
    dimension_x = len(floor[0])
    dimension_y = len(floor)
    for (_x, _y) in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if _x < 0 or _y < 0 or _x > dimension_x - 1 or _y > dimension_y - 1:
            continue
        surrounding_numbers.append(floor[_y][_x])
    return number < min(surrounding_numbers)


def count_around(x, y, level, floor, counted):
    """Count all around you that has higher level"""
    dimension_x = len(floor[0])
    dimension_y = len(floor)

    surrounding_count = 0
    for (_x, _y) in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if _x < 0 or _y < 0 or _x > dimension_x - 1 or _y > dimension_y - 1:
            continue
        if (_x, _y) in counted:
            continue
        if level < floor[_y][_x] < 9:
            surrounding_count += 1
            counted.add((_x, _y))
            surrounding_count += count_around(_x, _y, floor[_y][_x], floor, counted)
    return surrounding_count


def find_basin_size(x, y, floor):
    level = floor[y][x]
    basin_size = 1  # this
    counted = {(x, y)}
    basin_size += count_around(x, y, level, floor, counted)
    return basin_size


def main_1():
    with open("data.txt") as f:
        floor = []
        risk = 0
        for row in f.readlines():
            floor.append([int(c) for c in row.strip()])
        minimums = []
        for y in range(len(floor)):
            for x in range(len(floor[0])):
                if is_minimum(x, y, floor):
                    minimums.append((x, y))
                    risk += 1 + floor[y][x]
        print(f"{minimums=}!")
        print(f"{floor=}!")
        print(f"{risk=}")

        # Part two:
        basin_sizes = []
        for (x, y) in minimums:
            basin_size = find_basin_size(x, y, floor)
            if basin_size:
                basin_sizes.append(basin_size)

        basin_sizes.sort()
        basin_sizes = basin_sizes[-3:]

        print(f"{basin_sizes=}")

        result = math.prod(basin_sizes)
        print(f"{result}")


if __name__ == "__main__":

    main_1()
