#!/usr/bin/env python3

from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} points"


def heal(target: str, power: int) -> str:
    return f"Healing {target} for {power} HP"


# Isso é um caso de High Order Func:
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spells(target: str, power: int):
        return (spell1(target, power), spell2(target, power))
    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        return [s(target, power) for s in spells]
    return sequence


def main() -> None:

    targets = ["Giant", "Dragon", "Goblin", "Skeever"]
    combined = spell_combiner(fireball, heal)

    print("\nTesting spell combiner...")
    print(f"Combined spell result:{combined(targets[3], 50)}\n")

    print("Testing Amplifier damage...")
    i = 100
    amplifier = power_amplifier(fireball, i)
    amplified = amplifier(targets[2], 8)
    print(f"original: power = {i}, Amplified: {amplified}\n")

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    results = [sequence(target, 30) for target in targets]
    for r in results:
        print(*r)


if __name__ == "__main__":
    main()
