def main_1():
    last_number = None
    increased = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            number = int(line)
            if last_number:
                if number > last_number:
                    increased += 1

            last_number = number

    print(f"Number of increasd depths {increased}")


def main_2():
    """Sliding window of 3"""
    increased = 0
    number_list = []
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            number_list.append(int(line))

    window_list = []
    for i in range(len(number_list)):
        try:
            window_list.append(number_list[i] + number_list[i + 1] + number_list[i + 2])
        except Exception as exception:
            print("finished building windows_list")
    print(f"{window_list=}")
    last_number = None
    for number in window_list:
        if last_number:
            if number > last_number:
                increased += 1

        last_number = number

    print(f"Number of increasd depths {increased}")


if __name__ == "__main__":
    # main_1()
    main_2()
