#!/usr/bin/env python3

from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory, CreateFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory

from ex2.strategy import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    IvalidCreature,
)


Opponent = Tuple[CreateFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except IvalidCreature as e:
                raise IvalidCreature(f"Battle error, aborting tournament: {e}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    t0: List[Opponent] = [
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    try:
        battle(t0)
    except IvalidCreature as e:
        print(e)

    print()

    print("Tournament 1 (error)")
    t1: List[Opponent] = [
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ]
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    try:
        battle(t1)
    except IvalidCreature as e:
        print(e)

    print()

    print("Tournament 2 (multiple)")
    t2: List[Opponent] = [
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    try:
        battle(t2)
    except IvalidCreature as e:
        print(e)

    
if __name__ == "__main__":
    main()
