#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validated_result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} {validated_result}"


if __name__ == "__main__":
    light_spell_allowed_ingredients()
