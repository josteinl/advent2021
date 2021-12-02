def main_1():
    x = 0
    z = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            command, value = line.split()
            value = int(value)
            if command == "forward":
                x += value
            elif command == "up":
                z -= value
            elif command == "down":
                z += value

    print(f"{x=} * {z=} = {x*z}")


def main_2():
    """Sliding window of 3"""
    x = 0
    z = 0
    aim = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            command, value = line.split()
            value = int(value)
            if command == "forward":
                x += value
                z += aim * value
            elif command == "up":
                aim -= value
            elif command == "down":
                aim += value

    print(f"{x=} * {z=} = {x*z}")


if __name__ == "__main__":
    # main_1()
    main_2()
