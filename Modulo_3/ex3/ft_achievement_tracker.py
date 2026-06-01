#!/usr/bin/env python3

import random


achievements_list = [
        "Reader",
        "Oblicion Walker",
        "Dragonrider",
        "Legend",
        "Thu'um Master",
        "Bound Until Death",
        "Blessed",
        "War Hero",
        "The Temple of Miraak",
        "Glory of the Dead",
        "Soul Tear",
        "Kindred Judgement",
        "Auriel's Bow",
        ]

players = [
    "Alice",
    "Bob",
    "Carlos",
    "Jessica",
]


def gen_player_achievements() -> set:
    ach_length = random.randint(1, len(achievements_list))
    achievements_selected = set(random.sample(achievements_list, ach_length))

    return achievements_selected


def main() -> None:

    print("=== Achievement Tracker System ===\n")

    players_set = []
    for name in players:
        current_set = gen_player_achievements()
        players_set.append(current_set)
        print(f"Player {name}: {current_set}")

    all_distinct_achievements: set = set()
    for check_dist in players_set:
        all_distinct_achievements = all_distinct_achievements.union(check_dist)
    print(f"\nAll distinct achievements: {all_distinct_achievements}")

    common_achievements = all_distinct_achievements
    for check_dist in players_set:
        common_achievements = common_achievements.intersection(check_dist)
    print(f"\nCommon: {common_achievements}\n")

    i = 0
    for name in players:
        first_set = players_set[i]
        others: set = set()
        j = 0
        for new in players_set:
            if i != j:
                others = others.union(new)
            j += 1
        diff = first_set.difference(others)
        print(f"Only {name} has: {diff}")
        i += 1

    print()

    possible = set(achievements_list)
    i = 0
    for name in players:
        first_set = players_set[i]
        missing = possible.difference(first_set)
        print(f"{name} is missing: {missing}")
        i += 1


if __name__ == "__main__":
    main()
