#!/usr/bin/env python3

from collections.abc import Callable
from functools import wraps
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting before the function: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        final = time.time() - start
        print(f"Spell completed in {final:0.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = args[-1]
            if power < min_power:
                return "Insuficient power"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed (attempt {attempt}/{max_attempts})")
                    attempt += 1

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) > 2 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        time.sleep(0.101)
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    time.sleep(0.101)
    return "Result : Fireball cast!"


@retry_spell(3)
def test_retry() -> None:
    raise ValueError


def main() -> None:
    mage = MageGuild()
    print("============================")
    print("Testing spell timer...")
    result = fireball()
    print("Result:", result)
    print("============================")
    print("Testing Retry...")
    print(test_retry())
    print("Waaaaaaagh spelled !")
    print("============================")
    print("Testing MageGuild")
    print(mage.cast_spell("Thunder", 15))
    print(mage.cast_spell("fireball", 5))
    print(mage.validate_mage_name("Draco"))
    print(mage.validate_mage_name("h"))
    print("============================")


if __name__ == "__main__":
    main()
