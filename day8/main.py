from typing import List, Dict

len_dict = {2: 1, 4: 4, 3: 7, 7: 8}


def build_digits(signals: List[str]) -> Dict:
    signal_dict = {}  # set, value
    value_dict = {}  # value, string
    for signal in signals:
        if len(signal) in len_dict.keys():
            signal_dict[signal] = len_dict[len(signal)]
            value_dict[len_dict[len(signal)]] = set([digit for digit in signal])

    # acedgfb: 8 - OK
    # cdfbe: 5
    # gcdfa: 2
    # fbcad: 3
    # dab: 7 # OK
    # cefabd: 9
    # cdfgeb: 6
    # eafb: 4 # OK
    # cagedb: 0
    # ab: 1 # OK

    # cdfbe: 5
    # gcdfa: 2
    # fbcad: 3 OK
    # cefabd: 9
    # cdfgeb: 6 OK
    # cagedb: 0

    while len(value_dict.keys()) < 10:
        for signal in signals:
            if signal in signal_dict.keys():
                continue
            signal_set = set([digit for digit in signal])
            if len(signal_set) == 5:
                # Possible 2, 3, 5
                if value_dict[1] - signal_set == set():
                    signal_dict[signal] = 3
                    value_dict[3] = signal_set
                elif 6 in value_dict and (value_dict[1] - value_dict[6]).intersection(
                    signal_set
                ) == (value_dict[1] - value_dict[6]):
                    signal_dict[signal] = 2
                    value_dict[2] = signal_set
                elif 6 in value_dict and 3 in value_dict:
                    signal_dict[signal] = 5
                    value_dict[5] = signal_set

            elif len(signal_set) == 6:
                # Possible 0, 6, 9
                if 3 in value_dict and value_dict[3].union(value_dict[4]) == signal_set:
                    signal_dict[signal] = 9
                    value_dict[9] = signal_set
                elif value_dict[1] - signal_set != set():
                    signal_dict[signal] = 6
                    value_dict[6] = signal_set
                elif 9 in value_dict and 6 in value_dict:
                    signal_dict[signal] = 0
                    value_dict[0] = signal_set

    return signal_dict


def main():
    with open("data.txt") as f:
        total = 0
        result_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for row in f.readlines():
            signals, outputs = row.split("|")
            signals = signals.split()
            signals = ["".join(sorted(word)) for word in signals]
            outputs = outputs.split()
            outputs = ["".join(sorted(word)) for word in outputs]
            signal_dict = build_digits(signals)

            row_sum = 0
            for output in outputs:
                row_sum = row_sum * 10 + signal_dict[output]
            print(f"{row_sum=}")
            total += row_sum

    print(f"{total=}")


if __name__ == "__main__":
    main()
