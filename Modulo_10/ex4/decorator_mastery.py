#!/usr/bin/env python3

from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
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
        def wrapper(*args, **kwargs) -> Callable:
            power = args[-1]
            if power < min_power:
                return "Insuficient power"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return retry_spell(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt} / {max_attempts})"
                        )
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
    return "Fireball cast!"


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
    print(retry_spell(3)(mage.cast_spell)('Fireball', 5))
    print((mage.cast_spell)('Fireball', 15))
    print("============================")
    print(mage.cast_spell("Thunder", 15))
    print(mage.cast_spell("fireball", 5))


if __name__ == "__main__":
    main()
