#!/usr/bin/env python3

from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} points"


def heal(target: str, power: int) -> str:
    return f"Healing {target} for {power} HP"


# Isso é um caso de High Order Func:
def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spells


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int)\
     -> Callable[[str, int], str]:
    def amplifier(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable[[str, int], str],
                       spell: Callable[[str, int], str]) \
                       -> Callable[[str, int], str]:
    def conditional(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable[[str, int], str]])\
                   -> Callable[[str, int], str]:
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
