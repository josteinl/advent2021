import pytest

from main import explode, split


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


def test_split():
    # after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    # after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    # after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
    # after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    # after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    # after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    numbers = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    numbers, _ = explode(numbers)
    assert numbers == [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
    numbers, _ = explode(numbers)
    assert numbers == [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    numbers = split(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    numbers = split(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
    numbers, _ = explode(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
