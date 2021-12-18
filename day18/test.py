import pytest

from main import explode


@pytest.mark.parametrize(
    "numbers, exploded",
    [
        ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
        ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
        ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
        (
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        ),
    ],
)
def test_explode(numbers, exploded):
    result, _ = explode(numbers)
    assert result == exploded
