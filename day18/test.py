import pytest

from main import explode, split, add_numbers, calculate_magnitude


# fmt: off
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([[[[[9, 8], 1], 2], 3], 4],
         [[[[0, 9], 2], 3], 4]),
        ([7, [6, [5, [4, [3, 2]]]]],
         [7, [6, [5, [7, 0]]]]),
        ([[6, [5, [4, [3, 2]]]], 1],
         [[6, [5, [7, 0]]], 3]),
        (
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        ),
        ([[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], 1],
         [[[[4, 0], [5, 4]], [[0, [7, 6]], [9, 5]]], 1]),
        (
            [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]],
            [[[[4, 0], [5, 4]], [[0, [7, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
        ),
        ([[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[9, [7, 7]], [[0, [7, 8]], [11, 0]]]],
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[9, [7, 7]], [[7, 0], [19, 0]]]]
         ),
    ],
)
def test_explode(numbers, expected):
    result = explode(numbers)
    assert result == expected

# fmt: on


def test_split():
    # after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    # after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    # after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
    # after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    # after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    # after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    numbers = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    numbers = explode(numbers)
    assert numbers == [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
    numbers = explode(numbers)
    assert numbers == [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    numbers, _ = split(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    numbers, _ = split(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
    numbers = explode(numbers)
    assert numbers == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]


@pytest.mark.parametrize(
    "number_one, number_two, result",
    [
        (
            [[[[4, 3], 4], 4], [7, [[8, 4], 9]]],
            [1, 1],
            [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]],
        ),
        ([[[1, 1], [2, 2]], [3, 3]], [4, 4], [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]),
        (
            [[[[1, 1], [2, 2]], [3, 3]], [4, 4]],
            [5, 5],
            [[[[3, 0], [5, 3]], [4, 4]], [5, 5]],
        ),
        (
            [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]],
            [6, 6],
            [[[[5, 0], [7, 4]], [5, 5]], [6, 6]],
        ),
        (
            [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
            [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
            [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],
        ),
        (
            [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],
            [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
            [
                [[[6, 7], [6, 7]], [[7, 7], [0, 7]]],
                [[[8, 7], [7, 7]], [[8, 8], [8, 0]]],
            ],
        ),
        (
            [
                [[[6, 7], [6, 7]], [[7, 7], [0, 7]]],
                [[[8, 7], [7, 7]], [[8, 8], [8, 0]]],
            ],
            [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
            [
                [[[7, 0], [7, 7]], [[7, 7], [7, 8]]],
                [[[7, 7], [8, 8]], [[7, 7], [8, 7]]],
            ],
        ),
        (
            [
                [[[7, 0], [7, 7]], [[7, 7], [7, 8]]],
                [[[7, 7], [8, 8]], [[7, 7], [8, 7]]],
            ],
            [7, [5, [[3, 8], [1, 4]]]],
            [
                [[[7, 7], [7, 8]], [[9, 5], [8, 7]]],
                [[[6, 8], [0, 8]], [[9, 9], [9, 0]]],
            ],
        ),
        (
            [
                [[[7, 7], [7, 8]], [[9, 5], [8, 7]]],
                [[[6, 8], [0, 8]], [[9, 9], [9, 0]]],
            ],
            [[2, [2, 2]], [8, [8, 1]]],
            [[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]],
        ),
        (
            [[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]],
            [2, 9],
            [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]],
        ),
        (
            [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]],
            [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
            [
                [[[7, 8], [6, 7]], [[6, 8], [0, 8]]],
                [[[7, 7], [5, 0]], [[5, 5], [5, 6]]],
            ],
        ),
        (
            [
                [[[7, 8], [6, 7]], [[6, 8], [0, 8]]],
                [[[7, 7], [5, 0]], [[5, 5], [5, 6]]],
            ],
            [[[5, [7, 4]], 7], 1],
            [[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]],
        ),
        (
            [[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]],
            [[[[4, 2], 2], 6], [8, 7]],
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]],
        ),
    ],
)
def test_sum(number_one, number_two, result):
    number_sum = add_numbers(number_one, number_two)
    assert result == number_sum


@pytest.mark.parametrize(
    "number, expected",
    [
        ([9, 1], 29),
        ([1, 9], 21),
        ([[9, 1], [1, 9]], 129),
        ([[1, 2], [[3, 4], 5]], 143),
        ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
        ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
        ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
        ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
        ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
    ],
)
def test_magnitude(number, expected):
    calculated = calculate_magnitude(number)
    assert calculated == expected
