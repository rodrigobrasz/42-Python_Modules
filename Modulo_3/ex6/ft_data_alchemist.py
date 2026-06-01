#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    characters = [
        "Bob", "Charlie", "Bebedrigo", "leon", "Lidya", "Bebebea",
        "Palmeiras", "Andreas", "junior", "pedro",
    ]
    print(f"Initial Players: {characters}\n")

    c_all = [name.capitalize() for name in characters]
    print(f"New list with all names capitalized: {c_all}\n")

    cap_characters = [name for name in characters if name == name.capitalize()]
    print(f"New list of already-capitalized names: {cap_characters}\n")

    score = {c_all[i]: random.randint(1, 1000) for i in range(len(c_all))}
    print(f"Score Dict: {score}\n")

    avscore = round(sum(score.values()) / len(score), 2)
    print(f"Average score: {avscore}\n")

    high_scores = {x: score[x] for x in score if score[x] > avscore}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
