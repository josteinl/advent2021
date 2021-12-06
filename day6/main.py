from typing import List, Optional


class Fish:
    new_timer = 8
    reset_timer = 6

    def __init__(self, start_number):
        if start_number:
            self.timer = start_number
        else:
            self.timer = self.new_timer

    def tick(self):
        "Return Ture if spawning is needed"
        self.timer -= 1
        if self.timer < 0:
            self.timer = self.reset_timer
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.timer}"


def main_1():
    with open("data.txt") as f:
        start_numbers = [int(number) for number in f.readline().split(",")]

        fish = []
        for start_number in start_numbers:
            fish.append(Fish(start_number))

        print(f"init  {fish}")
        day = 0
        while day < 256:
            new_fish = []
            for f in fish:
                if f.tick():
                    new_fish.append(Fish(None))
            day += 1
            fish += new_fish
            # print(f"{day=} {fish}")

        result = len(fish)
        print(f"{result=}")


def main_2():
    """Try to optimize by grouping all fish that has the same timer"""
    with open("data.txt") as f:
        start_numbers = [int(number) for number in f.readline().split(",")]

        buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for start_number in start_numbers:
            buckets[start_number] += 1

        print(f"init  {buckets}")
        day = 0
        while day < 256:
            new_buckets = buckets[1:] + [0]
            new_buckets[6] += buckets[0]
            new_buckets[8] += buckets[0]
            buckets = new_buckets
            day += 1
            print(f"{day=} {buckets} {sum(buckets)=}")

        result = sum(buckets)
        print(f"{result=}")


if __name__ == "__main__":
    # main_1()
    main_2()
