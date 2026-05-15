def ft_plant_age() -> None:
    Age_1: int = int(input("Enter plant age in days: "))
    if (Age_1 > 60):
        print("Plant is ready to harvest !")
    else:
        print("Plant needs more time to grow.")
