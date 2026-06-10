#!/usr/bin/env python3


from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    start = initial_power

    def add_initial(amount: int) -> int:
        nonlocal start
        start += amount
        return start
    return add_initial


def enchantment_factory(enchantment_type: str) -> Callable:
    def new_enchantment(n_enchantment: str) -> str:
        return f"{enchantment_type} {n_enchantment}"
    return new_enchantment


def memory_vault() -> dict[str, Callable]:
    mem = {}

    def store(key: str, value: int) -> None:
        mem[key] = value

    def recall(key: str) -> int | str:
        return mem.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("=================================")
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    i = 1
    j = 1
    while i < 5:
        print(f"counter_a call {i}: {a()}")
        i += 1
    print()
    while j < 3:
        print(f"counter_b call {j}: {b()}")
        j += 1
    print("=================================")
    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base = 100, add 20: {acc(20)}")
    print(f"Base = 100, add 30: {acc(30)}")
    print("=================================")
    print("Testing enchantment factory...")
    ench = enchantment_factory("Flaming")
    ench2 = enchantment_factory("Frozen")
    print(ench("Sword"))
    print(ench2("Shield"))
    print("=================================")
    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']("secret", 42)
    print(f"Store 'secret': {vault['recall']('secret')}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('missing')}")
    print("=================================")


if __name__ == "__main__":
    main()
