#!/usr/bin/env python3

import sys


def main() -> None:

    print("=== Player Score Analytics ===")

    arg_len = len(sys.argv)
    valid_scores: list = []
    i = 1

    while i < arg_len:
        arg = sys.argv[i]
        try:
            vsocre = int(arg)
            valid_scores = valid_scores + [vsocre]
        except ValueError:
            print(f"Invalid parameter: {arg}")
        i += 1

    if len(valid_scores) == 0:
        print("No scores provided buddy try: "
              "python3 ft_score_analytics <Valid input1> <Valide input2>")
        return

    else:
        max_sore = max(valid_scores)
        min_score = min(valid_scores)
        sum_score = sum(valid_scores)
        len_player = len(valid_scores)
        print(f"Scores processed: {valid_scores}")
        print(f"Total Player: {len_player}")
        print(f"Total Score: {sum_score}")
        print(f"Avarage Score: {sum_score / len_player}")
        print(f"High Score: {max_sore}")
        print(f"Lowest Score: {min_score}")
        print(f"Score Range: {max_sore - min_score}")


if __name__ == "__main__":
    main()
