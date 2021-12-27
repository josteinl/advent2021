import pytest

from main import Board, solve

# fmt:off
@pytest.mark.parametrize(
    "rows, expected",
    [
        # (
        #     ["#############\n",
        #      "#.........A.#\n",
        #      "###.#B#C#D###\n",
        #      "  #A#B#C#D#\n",
        #      "  #########\n"],
        #     8
        # ),
        # (
        #     ["#############\n",
        #      "#...B.B.....#\n",
        #      "###A#.#C#D###\n",
        #      "  #A#.#C#D#\n",
        #      "  #########\n"],
        #     50
        # ),
        (
            ["#############",
             "#.....D.D.A.#",
             "###.#B#C#.###",
             "  #A#B#C#.#",
             "  #########"],
            3000+4000+8
        ),
    ]
)
# fmt:on
def test_final_steps(rows, expected):

    board = Board()

    for row in rows:
        board.add_row(row)

    cost = solve(board, cost_so_far=0)
    assert cost == expected
