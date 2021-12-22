from dataclasses import dataclass


class Reactor:
    def __init__(self):
        self.on_cubes = set()

    def number_on(self):
        return len(self.on_cubes)

    def boot_switch(
        self,
        switch: str,
        x_from: int,
        x_to: int,
        y_from: int,
        y_to: int,
        z_from: int,
        z_to: int,
    ):
        """ """
        for x in range(max(x_from, -50), min(x_to, 50) + 1):
            for y in range(max(y_from, -50), min(y_to, 50) + 1):
                for z in range(max(z_from, -50), min(z_to, 50) + 1):
                    if switch == "on":
                        self.on_cubes.add((x, y, z))
                    else:
                        self.on_cubes.discard((x, y, z))

    def switch(
        self,
        switch: str,
        x_from: int,
        x_to: int,
        y_from: int,
        y_to: int,
        z_from: int,
        z_to: int,
    ):
        """ """
        for x in range(x_from, x_to + 1):
            for y in range(y_from, y_to + 1):
                for z in range(z_from, z_to + 1):
                    if switch == "on":
                        self.on_cubes.add((x, y, z))
                    else:
                        self.on_cubes.discard((x, y, z))

    def execute_reboot_command(self, command):
        switch, dimensions = command.split(" ")
        x, y, z = dimensions.split(",")

        x_from, x_to = self.bake_dimensions(x)
        y_from, y_to = self.bake_dimensions(y)
        z_from, z_to = self.bake_dimensions(z)

        # If all out of valid range, then just skip the whole thing
        if x_from < -50 and x_to > 50:
            return
        if y_from < -50 and y_to > 50:
            return
        if z_from < -50 and z_to > 50:
            return

        self.boot_switch(switch, x_from, x_to, y_from, y_to, z_from, z_to)

    def execute_command(self, command):
        switch, dimensions = command.split(" ")
        x, y, z = dimensions.split(",")

        x_from, x_to = self.bake_dimensions(x)
        y_from, y_to = self.bake_dimensions(y)
        z_from, z_to = self.bake_dimensions(z)

        self.switch(switch, x_from, x_to, y_from, y_to, z_from, z_to)

    @staticmethod
    def bake_dimensions(dimension):
        _, from_to = dimension.split("=")

        d_from, d_to = from_to.split("..")
        d_from, d_to = int(d_from), int(d_to)

        if d_from > d_to:
            d_from, d_to = d_to, d_from
        return d_from, d_to


def main_1():
    reactor = Reactor()

    with open("data.txt") as f:
        for command in f.readlines():

            reactor.execute_reboot_command(command)

        print(f"{reactor.number_on()}")


def main_2():
    reactor = Reactor()

    with open("test_part_2_data.txt") as f:
        for command in f.readlines():

            reactor.execute_command(command)

        print(f"{reactor.number_on()}")


if __name__ == "__main__":
    main_1()
    # main_2()
