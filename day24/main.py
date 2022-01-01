from typing import List


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

        solution_found = False

        for model_number in range(99999999999999, 11111111111111, -1):
            inputs = [int(n) for n in list(str(model_number))]
            if 0 in inputs:
                # print(f"found 0")
                continue
            program.reset()
            result = program.run(inputs)
            if result["z"] == 0:
                solution_found = True
                print(f"Valid {model_number=}")
                break

        print(f"{program.variables=}")


if __name__ == "__main__":
    main()
