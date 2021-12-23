import abc
from typing import Optional, List
from copy import deepcopy


class Amphipods(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    @abc.abstractmethod
    def character(self):
        pass

    @property
    @abc.abstractmethod
    def cost(self):
        pass

    @property
    @abc.abstractmethod
    def targets(self):
        pass

    @property
    @abc.abstractmethod
    def allowed_position(self):
        pass

    def is_final_posision(self):
        return (self.x, self.y) in self.targets


class Amber(Amphipods):
    character = "A"
    cost = 1
    targets = [(3, 3), (3, 2)]
    allowed_position = [
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
        (3, 2),
        (3, 3),
    ]


class Bronze(Amphipods):
    character = "B"
    cost = 10
    targets = [(5, 3), (5, 2)]
    allowed_position = [
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
        (5, 2),
        (5, 3),
    ]


class Copper(Amphipods):
    character = "C"
    cost = 100
    targets = [(7, 3), (7, 2)]
    allowed_position = [
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
        (7, 2),
        (7, 3),
    ]


class Copper(Amphipods):
    character = "C"
    cost = 100
    targets = [(7, 3), (7, 2)]
    allowed_position = [
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
        (7, 2),
        (7, 3),
    ]


class Desert(Amphipods):
    character = "D"
    cost = 1000
    targets = [(9, 3), (9, 2)]
    allowed_position = [
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
        (9, 2),
        (9, 3),
    ]


char_class_mapping = {"A": Amber, "B": Bronze, "C": Copper, "D": Desert}

seen = set()


class Board:
    def __init__(self):
        self.rows = []
        self.pieces: List[Amphipods] = []

    def add_row(self, row):
        self.rows.append(row)
        y = len(self.rows) - 1
        for x, char in enumerate(row):
            if char in char_class_mapping.keys():
                amphipod = char_class_mapping[char](x, y)
                self.pieces.append(amphipod)

    def __repr__(self):
        board = ""
        for row in self.rows:
            board += row
        return board

    def possible_moves(self):
        result = []
        for i, piece in enumerate(self.pieces):
            # if in inner target room, skip
            if (piece.x, piece.y) in piece.targets[1]:
                continue
            # If piece in outer target room, and equal target in inner final room:
            if (piece.x, piece.y) in piece.targets[0] and self.rows[
                piece.targets[1][1]
            ][piece.targets[1][0]] == piece.character:
                continue

            for target in piece.allowed_position:
                # stand still, not a move
                if target == (piece.x, piece.y):
                    continue
                # Target occupied
                if self.rows[target[1]][target[0]] != ".":
                    continue
                # Try to go the way
                steps = self.step((piece.x, piece.y), target)
                if not steps:
                    continue

                cost = steps * piece.cost
                result.append((i, target, cost))

        return result

    def move(self, pice_index: int, move_to):
        pice = self.pieces[pice_index]
        self.rows[pice.y][pice.x] = "."
        pice.x, pice.y = move_to
        self.rows[pice.y][pice.x] = pice.character

    def step(self, from_position, to_position):
        """Cases.
        1 : start in room end in room
        2 : start in room end tunnel
        3 : start in tunnel end in room
        4 : start in tunnel end in tunnel

        Return number of steps, if path is open, otherwise return None
        """
        steps = 0
        current_x, current_y = from_position
        start_in_room = from_position[1] > 1
        end_in_room = to_position[1] > 1

        if start_in_room:
            # Walk out (up)
            for y in range(from_position[1] - 1, 1 - 1, -1):
                current_y = y
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1

        # walk in x direction
        if from_position[0] < to_position[0]:
            for x in range(from_position[0], to_position[0]):
                current_x = x
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1
        else:
            for x in range(to_position[0], from_position[0], -1):
                current_x = x
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1

        if end_in_room:
            # walk down
            for y in range(current_y, to_position[1]):
                current_y = y
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1
        return steps


def solve(board: Board, cost: int) -> Optional[int]:
    """Tries all possible moves for passed board state and returns the cost. If not possible to find a solution,
    then return None
    """
    if all([pice.is_final_posision() for pice in board.pieces]):
        return cost

    costs = []
    for piece_index, move_to, cost in board.possible_moves():
        new_board = deepcopy(board)
        new_board.move(piece_index, move_to)
        if cost is not None:
            costs.append(solve(new_board, cost))

    if not costs:
        return None

    return min(costs)


def main_1():

    board = Board()
    with open("test_data.txt") as f:
        for row in f.readlines():
            board.add_row(row)

        print(f"{board!r}")

    cost = solve(board, cost=0)
    print(f"{cost=}")


if __name__ == "__main__":
    main_1()
    # main_2()
