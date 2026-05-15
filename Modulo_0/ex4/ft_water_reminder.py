def ft_water_reminder() -> None:
    reminder: int = int(input("Days since last watering: "))
    if (reminder > 2):
        print("Water the plants!")
    else:
        print("plants are fine")
