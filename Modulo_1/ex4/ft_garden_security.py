#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return float(self._height)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(
                f"{self.get_name()}: Error, height can't be negative "
                f"({new_height}cm)\n"
                f"Height update rejected"
                  )
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"{self.get_name()}: Error, age can't be negative"
                f"({new_age} days)\n"
                f"Age updated rejected"
                )
            return
        self._age = new_age

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, {self._age} days old"
            )


def main() -> None:

    plant = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant Created: ", end="")
    plant.show()
    print()

    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm")
    plant.set_age(30)
    print(f"Age Updated: {plant.get_age()} days old")
    print()

    plant.set_age(-25)
    plant.set_height(-30)
    print()

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
