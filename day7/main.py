from typing import List, Optional


def calc_cost(pos, crab_list):
    cost = 0
    for i, value in enumerate(crab_list):
        cost += value * abs(pos - i)
    return cost


def main_1():
    with open("data.txt") as f:
        start_positions = [int(number) for number in f.readline().split(",")]

        dimension = max(start_positions)
        crab_list = [0] * (dimension + 1)
        cost_list = crab_list.copy()
        print(f"{crab_list=} ")

        for pos in start_positions:
            crab_list[pos] += 1

        for pos in range(len(cost_list)):
            cost_list[pos] = calc_cost(pos, crab_list)

        min_cost = min(cost_list)
        print(f"{min_cost=}")
        min_pos = cost_list.index(min_cost)

        print(f"{start_positions=} {dimension=}")
        print(f"{crab_list=} ")
        print(f"{cost_list=} ")
        print(f"{min_pos=} ")
        print(f"{cost_list[min_pos]=} ")


def calc_cost2(pos, crab_list, price_list):
    cost = 0
    for i, value in enumerate(crab_list):
        cost += value * price_list[abs(pos - i)]
    return cost


def main_2():
    with open("data.txt") as f:
        start_positions = [int(number) for number in f.readline().split(",")]

        dimension = max(start_positions)

        price_list = [n for n in range(dimension + 1)]
        print(f"{price_list=} ")
        for pos in price_list:
            if pos < 2:
                continue
            price_list[pos] += sum(price_list[pos - 1 : pos])
        print(f"{price_list=} ")

        crab_list = [0] * (dimension + 1)
        cost_list = crab_list.copy()
        print(f"{crab_list=} ")

        for pos in start_positions:
            crab_list[pos] += 1

        for pos in range(len(cost_list)):
            cost_list[pos] = calc_cost2(pos, crab_list, price_list)

        min_cost = min(cost_list)
        print(f"{min_cost=}")
        min_pos = cost_list.index(min_cost)

        print(f"{start_positions=} {dimension=}")
        print(f"{crab_list=} ")
        print(f"{cost_list=} ")
        print(f"{min_pos=} ")
        print(f"{cost_list[min_pos]=} ")


if __name__ == "__main__":
    # main_1()
    main_2()
