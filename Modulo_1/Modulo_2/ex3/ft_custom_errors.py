#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_unkow_plant() -> None:
    try:
        raise PlantError()
    except PlantError as e:
        print(f"alolaolaoal {e}")


def test_plant_error(plant_health: int) -> None:
    print("Testing PlantError...")
    try:
        if plant_health < 50:
            raise PlantError("The tomato plant is wilting!")
        print("Plant health is good.")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_tank(water_level: int) -> None:
    print("Testing WaterError...")
    try:
        if water_level < 10:
            raise WaterError("Not enough water in the tank!\n")
        elif water_level > 50:
            raise WaterError("The tank is full!")
        else:
            print("The water tank is in the normal level.")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_catch_all_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_plant_error(150)
    test_water_tank(-50)
    test_catch_all_garden_errors()
    test_unkow_plant()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
