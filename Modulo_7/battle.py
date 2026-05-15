#!/usr/bin/env python3

import ex0


def factory_checker(factory: ex0.CreateFactory) -> None:
    try:
        print("Testing factory")
        base = factory.create_base()
        evolved = factory.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())

    except Exception as e:
        print(f"Error {e}")


def battle_test(f1: ex0.CreateFactory, f2: ex0.CreateFactory) -> None:
    try:
        water_base = f2.create_base()
        fire_base = f1.create_base()
        print("Testing Battle")
        print(fire_base.describe())
        print(" vs.")
        print(water_base.describe())
        print(" fight!")
        print(fire_base.attack())
        print(water_base.attack())
    except Exception as e:
        print(f"Error {e}")


def main() -> None:
    fire = ex0.FlameFactory()
    factory_checker(fire)
    print()
    water = ex0.WaterFactory()
    factory_checker(water)
    print()
    battle_test(fire, water)


if __name__ == "__main__":
    main()
