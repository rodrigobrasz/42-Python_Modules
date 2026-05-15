#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print("Invalid height input")
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Invalid age input")
            return
        self._age = new_age

    def show(self) -> None:
        print(f"{self.get_name().capitalize()}: "
              f"{float(self.get_height()):.1f}cm, {self.get_age()} days old"
              )


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloomed(self, bloomed: bool) -> None:
        if bloomed is True:
            print(f"{self.get_name().capitalize()} is blooming beautifully!")

        elif bloomed is False:
            print(f"{self._name.capitalize()} has not bloomed yet")

        else:
            print("Invalid input")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, diameter: float) -> None:
        super().__init__(name, height, age)
        self._diameter = 0.0
        self.set_diameter(diameter)

    def set_diameter(self, new_diameter: float) -> None:
        self._diameter = new_diameter

    def get_diameter(self) -> float:
        return self._diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_diameter():.1f}cm")

    def shadow(self) -> None:
        print(f"The {self.get_name().capitalize()} now produces "
              f"a shade of {(self.get_height()):.1f}cm long and"
              f" {self.get_diameter():.1f}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, age, season: str, nutri: int) -> None:
        super().__init__(name, height, age)
        self.season = season
        self._nutri = nutri

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self._nutri}")

    def grow_vegetable(self) -> None:
        self.set_height(self.get_height() + 2.1)
        self.set_age(self.get_age() + 1)
        self._nutri += 1

    def get_nutri(self) -> int:
        return self._nutri


def main() -> None:
    rose = Flower("rose", 15, 10, "red")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloomed(False)
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloomed(True)
    print("")

    oak = Tree("Oak", 200, 365, 5)
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.shadow()
    print("")

    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    print("== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(1, 21):
        tomato.grow_vegetable()
    tomato.show()
    print("")


if __name__ == "__main__":
    main()
