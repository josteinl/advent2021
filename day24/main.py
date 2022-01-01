from typing import List, Set


class Program:
    variables = {}

    def __init__(self):
        self.instructions = []
        self.reset()

    @classmethod
    def reset(cls):
        cls.variables = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }

    def append(self, instruction):
        command = instruction.split()
        operation = command[0]
        parameter_1 = command[1]
        if operation == "inp":
            parameter_2 = None
        else:
            parameter_2 = command[2]

        if operation == "div" and parameter_2 == "1":
            # "div x 1" is a NOP
            return

        self.instructions.append((self.function_map(operation), parameter_1, parameter_2))

    def run(self, input_data: List):
        for command, parameter_1, parameter_2 in self.instructions:
            if command == self.__class__._inp:
                parameter_2 = input_data.pop(0)
            command(parameter_1, parameter_2)

        return self.variables

    @classmethod
    def function_map(cls, operation):
        return {
            "inp": cls._inp,
            "add": cls._add,
            "mul": cls._mul,
            "eql": cls._eql,
            "mod": cls._mod,
            "div": cls._div,
        }[operation]

    @classmethod
    def _inp(cls, variable: str, a: int):
        """
        inp a - Read an input value and write it to variable a.
        """
        cls.variables[variable] = a

    @classmethod
    def _add(cls, a, b):
        """
        add a b - Add the value of a to the value of b, then store the result in variable a.
        """
        value_a = cls.variables[a]

        if b in cls.variables.keys():
            value_b = cls.variables[b]
        else:
            value_b = int(b)

        cls.variables[a] = value_a + value_b

    @classmethod
    def _mul(cls, a, b):
        """
        mul a b - Multiply the value of a by the value of b, then store the result in variable a.
        """
        if b == 0:
            cls.variables[a] = 0

        value_a = cls.variables[a]

        if b in cls.variables.keys():
            value_b = cls.variables[b]
        else:
            value_b = int(b)

        cls.variables[a] = value_a * value_b

    @classmethod
    def _div(cls, a, b):
        """
        div a b - Divide the value of a by the value of b, truncate the result to an integer,
        then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
        """
        value_a = cls.variables[a]

        if b in cls.variables.keys():
            value_b = cls.variables[b]
        else:
            value_b = int(b)

        cls.variables[a] = value_a // value_b

    @classmethod
    def _mod(cls, a, b):
        """
        mod a b - Divide the value of a by the value of b, then store the remainder in variable a.
        (This is also called the modulo operation.)
        """
        value_a = cls.variables[a]

        if b in cls.variables.keys():
            value_b = cls.variables[b]
        else:
            value_b = int(b)

        cls.variables[a] = value_a % value_b

    @classmethod
    def _eql(cls, a, b):
        """
        eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
        """
        value_a = cls.variables[a]

        if b in cls.variables.keys():
            value_b = cls.variables[b]
        else:
            value_b = int(b)

        cls.variables[a] = [0, 1][value_a == value_b]


def main():
    with open("data.txt") as f:
        program = Program()
        for instruction in f.readlines():
            program.append(instruction)

        for model_number in range(99999999999999, 11111111111111, -1):
            inputs = [int(n) for n in list(str(model_number))]
            if 0 in inputs:
                # print(f"found 0")
                continue
            if inputs[8] not in valid_digits[9]:
                continue
            if inputs[9] not in valid_digits[10]:
                continue
            if inputs[10] not in valid_digits[11]:
                continue
            if inputs[11] not in valid_digits[12]:
                continue
            if inputs[12] not in valid_digits[13]:
                continue
            if inputs[13] not in valid_digits[14]:
                continue
            program.reset()
            result = program.run(inputs)
            if result["z"] == 0:
                print(f"Valid {model_number=}")
                break

            if not model_number % 11571211:
                print(f"{model_number}")
        print(f"{program.variables=}")


valid_digits = {
    14: {1, 2, 3, 4, 5},
    13: {1, 2, 3, 4, 5, 6, 7, 8},
    12: {2, 3, 4, 5, 6, 7, 8, 9},
    11: {1, 2, 3},
    10: {8, 9, 7},
    9: {5, 6, 7, 8, 9},
    8: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    7: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    6: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    5: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    4: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    3: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    2: {1, 2, 3, 4, 5, 6, 7, 8, 9},
    1: {1, 2, 3, 4, 5, 6, 7, 8, 9},
}


def test_digit(d, z_set):
    print(f"Digit position {d}")
    with open(f"data-digit{d}.txt") as f:
        program = Program()
        for instruction in f.readlines():
            program.append(instruction)

    result = {}
    for digit in range(1, 10):
        for z_in in z_set.keys():
            program.reset()
            run_result = program.run([z_in, digit])
            # print(f"{z=}, {digit=}, {result=}")
            if run_result["z"] in result:
                result[run_result["z"]]["z_in"].add(z_in)
                result[run_result["z"]]["digit"].add(digit)
            else:
                result[run_result["z"]] = {"z_in": set([z_in]), "digit": set([digit])}

    return result


def find_valid_digits():
    results = {}
    z = {0: 0}
    for digit in range(1, 15):
        z = test_digit(digit, z)
        results[digit] = z
        print(f"{len(z)}")

    valid_zeds = [0]
    for digit in range(14, 0, -1):
        print(f"Checking valid results for {digit=}:")
        digit_result = results[digit]
        next_layer = set()
        valid_digits = set()
        for zed in valid_zeds:
            if zed in digit_result:
                # print(f"{digit_result[zed]=}")
                next_layer.update(digit_result[zed]["z_in"])
                valid_digits.update(digit_result[zed]["digit"])

        valid_zeds = next_layer
        print(f"Valid digits for position {digit} is {valid_digits=}")


if __name__ == "__main__":
    main()
