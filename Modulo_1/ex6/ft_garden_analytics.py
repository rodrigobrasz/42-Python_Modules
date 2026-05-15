#!/usr/bin/env python3

class Plant:

    class PlantStatistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increasse_grow(self) -> None:
            self._grow_calls += 1

        def increasse_age(self) -> None:
            self._age_calls += 1

        def increasse_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age,"
                  f" {self._show_calls} show")

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self._height = 0.0
        self._plant_age = 0
        self.week_growth = float(0)
        self.set_height(height)
        self.set_age(plant_age)
        self._stats = Plant.PlantStatistics()

    def show(self) -> None:
        self._stats.increasse_show()
        print(f"{self.name.capitalize()}: {round(self._height, 1)}cm"
              f", {self._plant_age} days old")

    def grow(self, days: int) -> int:
        self._stats.increasse_grow()
        self._height += days
        return days

    def age(self, time: int) -> None:
        self._stats.increasse_age()
        for x in range(time):
            self._plant_age += 1

    def set_height(self, heigth: float) -> None:
        if heigth < 0:
            return
        self._height = float(heigth)

    def set_age(self, plant_age: int) -> None:
        if plant_age < 0:
            return
        self._plant_age = plant_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def check_age(age: int) -> bool:
        if age < 365:
            return False
        else:
            return True

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom_state = False

    def bloom(self) -> None:
        self.bloom_state = True

    def check_bloom(self) -> str:
        if self.bloom_state is True:
            return f"{self.name.capitalize()} is blooming beautifully!"
        return f"{self.name.capitalize()} has not bloomed yet"

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.check_bloom()}")


class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0
        self.shade_length = 0.0
        self.shade_width = 0.0

    def produce_shade(self) -> None:
        self.shade_length = self._height
        self.shade_width = self.trunk_diameter
        self.shade_calls += 1
        print(f"Tree {self.name} now produces a shade"
              f" of {round(self.shade_length, 1)}"
              f"cm long and {round(self.shade_width, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {(self.trunk_diameter):.1f}cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(f" {self.shade_calls} shade")


class Vegetable(Plant):
    def __init__(self, name, height, plant_age, harvest_season: str) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def nutrition(self) -> None:
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}"
              f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom_seeds(self, seed: int) -> None:
        super().bloom()
        self.seeds = seed

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    flower = Flower("rose", 15, 10, "red")
    tree = Tree("oak", 200, 365, 5)
    seed = Seed("sunflower", 80, 45, "yellow")
    anonymous = Plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? ->{Plant.check_age(30)} ")
    print(f"Is 400 days more tha a year? -> {Plant.check_age(400)}\n")

    print("=== Flower")
    flower.show()
    print("[statistics for Rose]")
    flower.display_stats()
    print("[asking the rose to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    print("[statistics for Rose]")
    flower.display_stats()

    print("\n=== Tree")
    tree.show()
    print("[statistics for Oak]")
    tree.display_stats()
    print("[asking the Oak to produce shade]")
    tree.produce_shade()
    print("[statistics for Oak]")
    tree.display_stats()

    print("\n=== Seed")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.bloom()
    seed.grow(30)
    seed.age(20)
    seed.bloom_seeds(42)
    seed.show()
    print("[statistics for Sunflower]")
    seed.display_stats()

    print("\n=== Anonymous")
    anonymous.show()
    print("[statistics for anonymous]")
    anonymous.display_stats()


if __name__ == "__main__":
    main()
