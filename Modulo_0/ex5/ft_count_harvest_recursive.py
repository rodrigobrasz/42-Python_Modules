def ft_count_harvest_recursive() -> None:
    i = int(input("Days until harvest: "))

    def day(x: int):
        print("Day", x)
        if x < i:
            day(x + 1)

    day(1)
    print("Harvest time!")

ft_count_harvest_recursive()
