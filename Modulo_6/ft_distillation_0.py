#!/usr/bin/env python3

from alchemy import potions


if __name__ == "__main__":
    print("=== Distillation 0 ===\n")
    print("Direct access to alchemy/potions.py\n")
    print(f"Testing healing_potions: {potions.healing_potion()}")
    print(f"Testing strength_potion: {potions.strength_potion()}")
