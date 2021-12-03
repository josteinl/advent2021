from typing import List


def main_1():
    gamma = ""
    epsilon = ""
    bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_number = 1
    with open("data.txt") as f:
        for line in f.readlines():
            line_number += 1
            for i, bit in enumerate(line):
                if bit == "1":
                    bit_count[i] += 1
        for bit in bit_count:
            if bit > line_number / 2:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(f"{gamma=} * {epsilon=} = {gamma*epsilon}")


def count(lines, bit_pos, keep_equal):
    """
    if keep_equal = "1", then return the most number of bits
    otherwise return the fewest number of bits
    """
    count_bits = 0
    for line in lines:
        if line[bit_pos] == keep_equal:
            count_bits += 1

    if keep_equal == "0":
        # Return fewest
        if count_bits <= len(lines) / 2:
            return "0"
        else:
            return "1"
    else:
        # Return most
        if count_bits >= len(lines) / 2:
            return "1"
        else:
            return "0"


def remove(lines, keep_equal: str) -> List[str]:
    number_of_bits = len(lines[0].strip())
    while len(lines) > 1:
        for bit_pos in range(number_of_bits):
            keep = count(lines, bit_pos, keep_equal)
            for i in range(len(lines) - 1, -1, -1):
                if len(lines) == 1:
                    return lines
                if keep != lines[i][bit_pos]:
                    del lines[i]
    return lines


def main_2():
    with open("data.txt") as f:
        oxygen_lines = f.readlines()
        scrubber_lines = oxygen_lines.copy()

        oxygen_lines = remove(oxygen_lines, keep_equal="1")
        scrubber_lines = remove(scrubber_lines, keep_equal="0")

    oxygen = int(oxygen_lines[0], 2)
    scrubber = int(scrubber_lines[0], 2)
    print(f"{oxygen=} * {scrubber=} = {oxygen*scrubber}")


if __name__ == "__main__":
    # main_1()
    main_2()
