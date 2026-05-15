#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def show(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.days_old} days)")


def main() -> None:
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")

    for name, height, age in plant_data:
        Plant(name, height, age).show()


if __name__ == "__main__":
    main()
