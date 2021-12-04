from typing import List, Optional


class Board:
    def __init__(self, drawn_numbers):
        self.rows = []
        self.columns = []
        self.dimension = None
        self.drawn_numbers = {}
        self.drawn_numbers = set(drawn_numbers)

    def add_row(self, row):
        if not self.dimension:
            self.dimension = len(row)
            for i in range(self.dimension):
                self.columns.append([])

        self.rows.append(row)
        for i, number in enumerate(row):
            self.columns[i].append(number)

    def add_drawn_number(self, number):
        self.drawn_numbers.add(number)

    def bingo(self) -> (bool, Optional[List[int]]):
        for row in self.rows:
            if not (set(row) - self.drawn_numbers):
                return True, row

        for column in self.columns:
            if not (set(column) - self.drawn_numbers):
                return True, column

        return False, None

    def sum_all_unmarked(self):
        sum = 0
        for row in self.rows:
            for number in row:
                if number not in self.drawn_numbers:
                    sum += number

        return sum


def main_1():
    with open("test_data.txt") as f:
        random_numbers = [int(number) for number in f.readline().split(",")]

        boards = []
        for line in f.readlines():

            if not line.split():
                # Empty line
                board = Board(random_numbers[:5])
                boards.append(board)
            else:
                board.add_row([int(number) for number in line.split()])

        for drawn_number in random_numbers[5:]:
            for board in boards:
                board.add_drawn_number(drawn_number)
                bingo, row = board.bingo()
                if bingo:
                    break
            if bingo:
                break

        if bingo:
            score = board.sum_all_unmarked()
            print(f"{row=}")
            print(f"sum of row: {score}")
            print(f"{drawn_number=}")
            score *= drawn_number
            print(f"Bingo: {score=}")
        else:
            print(f"No bingo found!")


def main_2():
    with open("data.txt") as f:
        random_numbers = [int(number) for number in f.readline().split(",")]

        boards = []
        for line in f.readlines():

            if not line.split():
                # Empty line
                board = Board(random_numbers[:5])
                boards.append(board)
            else:
                board.add_row([int(number) for number in line.split()])

        while len(boards) > 1:
            for drawn_number in random_numbers[5:]:
                remove_indexes = []
                for i, board in enumerate(boards):
                    board.add_drawn_number(drawn_number)
                    bingo, row = board.bingo()
                    if bingo:
                        remove_indexes.append(i)

                for i in remove_indexes[::-1]:
                    board = boards.pop(i)

                if len(boards) < 1:
                    break

        if bingo:
            score = board.sum_all_unmarked()
            print(f"{row=}")
            print(f"sum of row: {score}")
            print(f"{drawn_number=}")
            score *= drawn_number
            print(f"Bingo: {score=}")
        else:
            print(f"No bingo found!")


if __name__ == "__main__":
    # main_1()
    main_2()
