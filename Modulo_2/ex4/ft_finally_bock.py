#!/usr/bin/env python3

class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid Plant name: '{plant_name}' ")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    print("=== Garden Watering system ===\n")

    print("Testing valid plants...")
    test_watering_system(valid_plants)

    print("\nTesting invalid plants...")
    test_watering_system(invalid_plants)

    print("\ncleanup always happens even with errors!")


if __name__ == "__main__":
    main()
