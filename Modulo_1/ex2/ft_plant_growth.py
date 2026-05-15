#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float,
                 days_old: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> str:
        return f"{self.name}, {self.height:.1f}cm, {self.days_old} days old"


def main() -> None:
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25, 20, 0.8)
    plant2 = Plant("Sunflower", 15, 15, 1.6)
    start_rose = plant.height
    start_sunflower = plant2.height

    print("=== Day 1 ===")
    print(plant.show())
    print(plant2.show())
    for day in range(2, 8):
        print(f"=== Day {day} ===\n")
        plant2.grow()
        plant2.age()
        plant.grow()
        plant.age()
        print(f"{plant.show()}")
        print(f"{plant2.show()}\n")

    increase_week_rose = plant.height - start_rose
    increase_week_sunflower = plant2.height - start_sunflower
    print(f"Rose growth this week: {increase_week_rose:.1f}")
    print(f"Sunflower growth this week: {increase_week_sunflower:.1f}")


if __name__ == "__main__":
    main()
