def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(seed_type.capitalize(), "seed: ", end=" ")
        print(quantity, unit, "Avaliabe")
    elif (unit == "grams"):
        print(seed_type.capitalize(), "seed: ", end=" ")
        print(quantity, unit, "Total")
    elif (unit == "area"):
        print(seed_type.capitalize(), "seed: ", end=" ")
        print("covers", quantity, "square meters")
    else:
        print("Unkow unit type")
