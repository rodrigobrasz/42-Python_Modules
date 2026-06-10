#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)

    if operation == "multply":
        return reduce(operator.mul, spells)

    if operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)

    if operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)

    raise ValueError("Error")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_element = partial(base_enchantment, 50, "fire")
    ice_element = partial(base_enchantment, 50, "ice")
    shock_element = partial(base_enchantment, 50, "shock")

    return {
        "fire": fire_element,
        "ice": ice_element,
        "shock": shock_element
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} is enchanted with {element} with {power} magic points!"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(value: Any):
        return ("Unknown spell type")

    @dispatch.register(int)
    def _1(value: int):
        return (f"{value}")

    @dispatch.register(str)
    def _2(value: str):
        return (f"{value}")

    @dispatch.register(list)
    def _3(value: list):
        return (f"{str(len(value))}")

    return dispatch


def main() -> None:
    print("===============================")
    print("Testing spell reducer...")
    spells = [10, 20, 60]
    print(f"List: {spells}")
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))
    print("===============================")
    print("Testing Partial Enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("katana"))
    print(enchanters["ice"]("crossbow"))
    print(enchanters["shock"]("hammer"))
    print("===============================")
    print("Testing Fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15)", memoized_fibonacci(15))
    print("===============================")
    dispacher = spell_dispatcher()
    spells = ["ice", "fire", "thunder"]
    print("Damage spell:", dispacher(42))
    print("Enchantment:", dispacher("fireball"))
    print("Multi-cast", dispacher(spells))
    print(dispacher(2.6))
    print("===============================")


if __name__ == "__main__":
    main()
