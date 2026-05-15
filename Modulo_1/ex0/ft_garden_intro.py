#!/usr/bin/env python3

def ft_garden_intro(name: str, age: int, height: int) -> None:

    print("=== Welcome to My Garden ===")
    print(
        f"Plant: {name}\n"
        f"Height: {height}cm\n"
        f"Age: {age} days\n"
        "\n=== End of Program ==="
        )


if __name__ == "__main__":
    ft_garden_intro("Rose", 30, 25)
