import pytest

from day24.main import Program


# fmt:off
@pytest.mark.parametrize(
    "instructions, inputs",
    [(("inp x",
       "mul x -1"),
      [5, 4, -3])],
)
# fmt:on
def test_negative_alu(instructions, inputs):
    program = Program()
    for instruction in instructions:
        program.append(instruction)

    for _input in inputs:
        result = program.run([_input])
        assert result["x"] == -_input


# fmt:off
@pytest.mark.parametrize(
    "instructions, inputs, expected_z",
    [(("inp z",
       "inp x",
       "mul z 3",
       "eql z x"),
      [5, 15], 1),
     (("inp z",
       "inp x",
       "mul z 3",
       "eql z x"),
      [3, 15], 0)
     ],
)
# fmt:on
def test_three_times_larger_alu(instructions, inputs, expected_z):
    """
    ALU program which takes two input numbers, then sets z to 1 if the second input number is three times larger than
    the first input number, or sets z to 0 otherwise:
    """
    program = Program()
    for instruction in instructions:
        program.append(instruction)

    result = program.run(inputs)
    assert result["z"] == expected_z


# fmt:off
@pytest.mark.parametrize(
    "input, expected_w, expected_x, expected_y, expected_z",
    [(8, 1, 0, 0, 0),
     (4, 0, 1, 0, 0),
     (2, 0, 0, 1, 0),
     (1, 0, 0, 0, 1),
     (9, 1, 0, 0, 1),
     (13, 1, 1, 0, 1),
     ]
)
def test_bit_fickling(input, expected_w, expected_x, expected_y, expected_z):
    instructions = (
        "inp w",
        "add z w",
        "mod z 2",
        "div w 2",
        "add y w",
        "mod y 2",
        "div w 2",
        "add x w",
        "mod x 2",
        "div w 2",
        "mod w 2",
      )
# fmt:on
    program = Program()
    for instruction in instructions:
        program.append(instruction)

    result = program.run([input])
    assert result["w"] == expected_w
    assert result["x"] == expected_x
    assert result["y"] == expected_y
    assert result["z"] == expected_z
