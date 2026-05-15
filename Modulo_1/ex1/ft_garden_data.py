#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self.height}cm, "
            f"{self.age} days old"
            )


def main() -> None:
    plants_list = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 80, 45),
        Plant("Sunflower", 15, 120),
    ]
    rose, cactus, sunflower = plants_list
    print("=== Garden Plant Registry ===")
    for plants in plants_list:
        plants.show()


if __name__ == "__main__":
    main()
