import abc
from typing import Optional, List
from copy import deepcopy

# The index for inner and outer rooms
OUTER_ROOM = 3
OUTER_MIDDLE_ROOM = 2
INNER_MIDDLE_ROOM = 1
INNER_ROOM = 0
X = 0
Y = 1


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

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.x}, {self.y})>"


class Amber(Amphipods):
    character = "A"
    cost = 1
    targets = [(3, 5), (3, 4), (3, 3), (3, 2)]
    allowed_position = [
        (3, 5),
        (3, 4),
        (3, 3),
        (3, 2),
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    ]


class Bronze(Amphipods):
    character = "B"
    cost = 10
    targets = [(5, 5), (5, 4), (5, 3), (5, 2)]
    allowed_position = [
        (5, 5),
        (5, 4),
        (5, 3),
        (5, 2),
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    ]


class Copper(Amphipods):
    character = "C"
    cost = 100
    targets = [(7, 5), (7, 4), (7, 3), (7, 2)]
    allowed_position = [
        (7, 5),
        (7, 4),
        (7, 3),
        (7, 2),
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    ]


class Copper(Amphipods):
    character = "C"
    cost = 100
    targets = [(7, 5), (7, 4), (7, 3), (7, 2)]
    allowed_position = [
        (7, 5),
        (7, 4),
        (7, 3),
        (7, 2),
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    ]


class Desert(Amphipods):
    character = "D"
    cost = 1000
    targets = [(9, 5), (9, 4), (9, 3), (9, 2)]
    allowed_position = [
        (9, 5),
        (9, 4),
        (9, 3),
        (9, 2),
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    ]


char_class_mapping = {"A": Amber, "B": Bronze, "C": Copper, "D": Desert}

seen_cost = {}


class Board:
    def __init__(self, test: bool = False):
        self.rows = []
        self.pieces: List[Amphipods] = []
        self.test = test

        # Record all seen evaluated board situations, and skip if seen again
        self.seen = set()

    def add_row(self, row):
        self.rows.append(row)
        y = len(self.rows) - 1
        for x, char in enumerate(row):
            if char in char_class_mapping.keys():
                amphipod = char_class_mapping[char](x, y)
                self.pieces.append(amphipod)

        # self.pieces.sort(key=lambda x: x.character)

    def board_state(self) -> frozenset:
        return frozenset([(piece.character, piece.x, piece.y) for piece in self.pieces])

    def __repr__(self):
        board = ""
        for row in self.rows:
            board += row
        return board

    def possible_moves(self):
        """
        New possible moves, read the rules again, and it is not allowed to move in the hallway!
        """
        result = []
        for i, piece in enumerate(self.pieces):
            # fmt:off
            # if current piece in inner target room, skip, because target is reached
            if (piece.x, piece.y) == piece.targets[INNER_ROOM]:
                continue

            # If current piece in inner middle target room, and equal target in inner final room, target reached
            if (piece.x, piece.y) == piece.targets[INNER_MIDDLE_ROOM] and \
                    self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] == piece.character:
                continue

            # If current piece in outer middle target room, and equal piece in inner middle and inner final room,
            # target reached
            if (piece.x, piece.y) == piece.targets[OUTER_MIDDLE_ROOM] and \
                    self.rows[piece.targets[INNER_MIDDLE_ROOM][Y]][piece.targets[INNER_MIDDLE_ROOM][X]] == piece.character and \
                    self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] == piece.character:
                continue

            # If current piece in outer target room, and equal target in inner final room, target reached
            if (piece.x, piece.y) == piece.targets[OUTER_ROOM] and \
                    self.rows[piece.targets[OUTER_MIDDLE_ROOM][Y]][piece.targets[OUTER_MIDDLE_ROOM][X]] == piece.character and \
                    self.rows[piece.targets[INNER_MIDDLE_ROOM][Y]][piece.targets[INNER_MIDDLE_ROOM][X]] == piece.character and \
                    self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] == piece.character:
                continue
            # fmt:on

            for target in piece.allowed_position:
                # Target occupied
                if self.rows[target[Y]][target[X]] != ".":
                    continue

                # If both target.y and piece.y == 1, it is not allowed to move in the hallway, only move in and out
                if target[Y] == 1 == piece.y:
                    continue

                # fmt:off
                # target is outer target room, but outer middle, inner middle and inner target room is not occupied by
                # correct piece:
                if target == piece.targets[OUTER_ROOM] and \
                        self.rows[piece.targets[OUTER_MIDDLE_ROOM][Y]][piece.targets[OUTER_MIDDLE_ROOM][X]] != piece.character and \
                        self.rows[piece.targets[INNER_MIDDLE_ROOM][Y]][piece.targets[INNER_MIDDLE_ROOM][X]] != piece.character and \
                        self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] != piece.character:
                    continue

                # if target is outer_middle_room
                if target == piece.targets[OUTER_MIDDLE_ROOM] and \
                        self.rows[piece.targets[OUTER_ROOM][Y]][piece.targets[OUTER_ROOM][X]] != '.' and \
                        self.rows[piece.targets[INNER_MIDDLE_ROOM][Y]][piece.targets[INNER_MIDDLE_ROOM][X]] != piece.character and \
                        self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] != piece.character:
                    continue

                if target == piece.targets[INNER_MIDDLE_ROOM] and \
                        self.rows[piece.targets[OUTER_ROOM][Y]][piece.targets[OUTER_ROOM][X]] != '.' and \
                        self.rows[piece.targets[OUTER_MIDDLE_ROOM][Y]][piece.targets[OUTER_MIDDLE_ROOM][X]] != '.' and \
                        self.rows[piece.targets[INNER_ROOM][Y]][piece.targets[INNER_ROOM][X]] != piece.character:
                    continue
                # fmt:on

                # Try to go the way
                steps = self.step((piece.x, piece.y), target)
                if not steps:
                    continue

                cost = steps * piece.cost
                result.append((i, target, cost))

        return result

    def move(self, piece_index: int, move_to):
        piece = self.pieces[piece_index]
        self.rows[piece.y] = self.rows[piece.y][: piece.x] + "." + self.rows[piece.y][piece.x + 1 :]
        piece.x, piece.y = move_to
        self.rows[piece.y] = self.rows[piece.y][: piece.x] + piece.character + self.rows[piece.y][piece.x + 1 :]
        # # When piece in final position, then remove it from self.piece (faster future lookup and smaller board state)
        # if (piece.x, piece.y) in self.pieces.targets:
        #     del self.pieces[piece_index]

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
        start_in_room = from_position[Y] > 1
        end_in_room = to_position[Y] > 1

        if start_in_room:
            # Walk out (up)
            for y in range(from_position[Y] - 1, 1 - 1, -1):
                current_y = y
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1

        # walk in x direction
        if from_position[X] < to_position[X]:
            for x in range(from_position[X] + 1, to_position[X] + 1):
                current_x = x
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1
        else:
            for x in range(from_position[X] - 1, to_position[X] - 1, -1):
                current_x = x
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1

        if end_in_room:
            # walk down
            for y in range(current_y + 1, to_position[Y] + 1):
                current_y = y
                if self.rows[current_y][current_x] != ".":
                    return None
                steps += 1
        return steps


minimum_solution_cost = None


def solve(board: Board, cost_so_far: int, level=0) -> Optional[int]:
    """Tries all possible moves for passed board state and returns the cost. If not possible to find a solution,
    then return None
    """
    global minimum_solution_cost

    # if level > 8:
    #     return None

    if minimum_solution_cost is not None and cost_so_far >= minimum_solution_cost:
        # print(f"{cost_so_far=} >= {minimum_solution_cost=}, abort branch")
        return None

    if all([pice.is_final_posision() for pice in board.pieces]):
        print(f"{'==' * 20}")
        print(f"Found solution for")
        print(f"{level=} {cost_so_far=} {minimum_solution_cost=}:")
        print(f"{board!r}")
        print(f"{'=='*20}")
        return cost_so_far

    board_state = board.board_state()
    if board_state in board.seen:
        # print(f"Above seen before. Ignore branch!")
        return None

    if board_state in seen_cost.keys() and cost_so_far >= seen_cost[board_state]:
        return None

    seen_cost[board_state] = cost_so_far
    board.seen.add(board_state)

    costs = []
    possible_moves = board.possible_moves()
    for piece_index, move_to, move_cost in possible_moves:
        new_board = deepcopy(board)
        new_board.move(piece_index, move_to)
        # if level == 0:
        # print(f"{'--'*20}")
        # print(f"{level=} {cost_so_far=} {minimum_solution_cost=}:")
        # print(
        #     f"move {board.pieces[piece_index].character} ({board.pieces[piece_index].x}, {board.pieces[piece_index].y}) -> {move_to!r}"
        # )
        # print(f"{new_board!r}")
        total_cost = solve(new_board, cost_so_far + move_cost, level=level + 1)
        if total_cost is not None:
            if minimum_solution_cost is None:
                minimum_solution_cost = total_cost
            else:
                minimum_solution_cost = min(total_cost, minimum_solution_cost)
            costs.append(total_cost)

    if not costs:
        return None

    return min(costs)


def main_1():

    board = Board()
    with open("data_part2.txt") as f:
        for row in f.readlines():
            board.add_row(row)
        # board.remove_pices_in_final_position()
        print(f"Start board:")
        print(f"{board!r}")
        print(f"***************************************")

    cost = solve(board, cost_so_far=0)
    print(f"{cost=}")


if __name__ == "__main__":
    main_1()
    # main_2()
