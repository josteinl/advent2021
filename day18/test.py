from main import explode


def test_explode():
    # numbers = [[[[[9, 8], 1], 2], 3], 4]
    # exploded = [[[[0, 9], 2], 3], 4]
    # assert (exploded, True) == explode(numbers)
    # numbers = [7, [6, [5, [4, [3, 2]]]]]
    # exploded = [7, [6, [5, [7, 0]]]]
    # assert (exploded, True) == explode(numbers)
    numbers = [[6, [5, [4, [3, 2]]]], 1]
    exploded = [[6, [5, [7, 0]]], 3]
    numbers, _ = explode(numbers)
    numbers = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
    exploded = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    assert (exploded, True) == explode(numbers)
    numbers = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    exploded = [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
    assert (exploded, True) == explode(numbers)
