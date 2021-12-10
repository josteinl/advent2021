from statistics import median
from typing import List


def main_1():
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            stack = []
            for char in line:
                if char in brackets.keys():
                    stack.append(char)
                else:
                    pre_char = stack.pop()
                    if brackets[pre_char] != char:
                        print(f"error {char}")
                        score += points[char]
            print(f"{line=}")

    print(f"{score=}")


def main_2():
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = []
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            stack = []
            line_score = 0
            dismiss_line = False
            for char in line:
                if dismiss_line:
                    continue
                if char in brackets.keys():
                    stack.append(char)
                else:
                    pre_char = stack.pop()
                    if brackets[pre_char] != char:
                        dismiss_line = True
                        continue

            if not dismiss_line:
                for char in stack[::-1]:
                    line_score = line_score * 5 + points[char]
                score.append(line_score)

    score.sort()
    print(f"{score=}")
    middle = (len(score)) / 2
    print(f"{len(score)=}")
    print(f"{middle=}")
    middle = int(middle)
    print(f"{middle=}")
    final_score = score[middle]
    print(f"{final_score=}")
    print(f"{score[int(len(score)/2)]=}")
    print(f"{score[int(len(score)/2)]=}")
    final_score = median(score)
    print(f"{final_score=}")


if __name__ == "__main__":
    # main_1()
    main_2()
    # failes 2170604194
