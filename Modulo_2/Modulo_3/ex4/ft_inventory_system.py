#!/usr/bin/env python3

import sys

args = sys.argv[1:]


def create_inventory() -> dict:

    main_inventory = {}

    if len(args) == 0:
        return main_inventory
    print("=== Inventory System Analysis ===")

    for itens in args:
        try:
            key, value = itens.split(":")
            if key in main_inventory:
                print(f"Redundent item '{key}' - discarding")
                continue
            try:
                main_inventory[key] = int(value)
            except ValueError as e:
                print(f"Quantity error for 'key' : {e}")
        except ValueError:
            print(f"Error - Invalide parameter '{itens}'")

    return main_inventory


def main() -> None:
    loot = create_inventory()
    if not loot:
        print("The game has started so your inventory is empty ;)")
        return
    total_values = sum(loot.values())
    total_keys = len(sys.argv) - 1
    abundant_item = None
    least_abundant = None
    max_value = None
    min_value = None

    print(f"Got Iventory{loot}")
    print(f"Total quantity of the {total_keys} items:{total_values}")

#   Percentage:
    for item in loot.keys():
        percent = (loot[item] / total_values) * 100
        print(f"Item {item} represents {round(percent, 1)}%")

#   Max/Min
    for item, qty in loot.items():
        if max_value is None or qty > max_value:
            max_value = qty
            abundant_item = item
        if min_value is None or qty < min_value:
            min_value = qty
            least_abundant = item
    print(f"Item most abundat: {abundant_item} with quantity: {max_value}")
    print(f"Item Least abundant: {least_abundant} with quantity: {min_value}")

#   Update
    loot.update({"Zenith": 1})
    print(f"Updated inventory: {loot}")


if __name__ == "__main__":
    main()
