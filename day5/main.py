from typing import List, Optional


class Diagram:
    def __init__(self):
        self._diagram = {}

    def add_point(self, x, y):
        if (x, y) in self._diagram:
            self._diagram[(x, y)] += 1
        else:
            self._diagram[(x, y)] = 1

    def delta(self, x1, x2):
        if x1 == x2:
            return 0
        if x1 < x2:
            return 1
        return -1

    def add(self, f_x, f_y, t_x, t_y):

        delta_x = self.delta(f_x, t_x)
        delta_y = self.delta(f_y, t_y)
        x = f_x
        y = f_y
        while True:
            self.add_point(x, y)
            x += delta_x
            y += delta_y

            if x == t_x and y == t_y:
                self.add_point(x, y)
                break

    def number_of_crossings(self):
        count = 0
        for key, value in self._diagram.items():
            if value >= 2:
                count += 1
        return count


def main_1():
    with open("data.txt") as f:
        diagram = Diagram()
        for line in f.readlines():
            from_x_y, to_x_y = line.split(" -> ")
            from_x_y = from_x_y.split(",")
            to_x_y = to_x_y.split(",")
            diagram.add(
                int(from_x_y[0]), int(from_x_y[1]), int(to_x_y[0]), int(to_x_y[1])
            )

        count = diagram.number_of_crossings()
        print(f"Number of crossings {count}!")
        # 21059 wrong


def main_2():
    with open("data.txt") as f:
        print(f"No bingo found!")


if __name__ == "__main__":

    main_1()
    # main_2()
