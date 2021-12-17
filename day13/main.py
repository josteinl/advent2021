from typing import List, Optional

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class Board:
    def __init__(self):
        self.dots = set()
        self.dimension = None

    def add_point(self, point: Point):
        self.dots.add(point)

    def fold(self, direction, value):
        for dot in self.dots.copy():
            if getattr(dot, direction) > value:
                self.dots.remove(dot)
                distance = getattr(dot, direction) - value
                if direction == "x":
                    self.dots.add(Point(dot.x - distance * 2, dot.y))
                else:
                    self.dots.add(Point(dot.x, dot.y - distance * 2))

    def __repr__(self):
        max_x = max([dot.x for dot in self.dots])
        max_y = max([dot.y for dot in self.dots])
        result = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for dot in self.dots:
            # result[dot.x][dot.y] = "#"
            result[dot.y][dot.x] = "#"
        result_string = ""
        for row in result:
            result_string += "".join(row) + "\n"
        return result_string

    def num_dots(self):
        return len(self.dots)


def main_1():
    with open("test_data.txt") as f:
        board = Board()
        data_part = True
        for row in f.readlines():
            row = row.strip()
            if data_part:
                if row == "":
                    data_part = False
                    print(f"board before any folding:")
                    print(f"{board!r}")
                    continue
                x, y = row.split(",")
                board.add_point(Point(int(x), int(y)))
            else:
                words = row.split()
                direction, value = words[-1].split("=")
                board.fold(direction, int(value))
                print(f"{board.num_dots()}")
                print(f"{board!r}")

    print(f"{board.num_dots()}")


if __name__ == "__main__":
    main_1()
    # main_2()
