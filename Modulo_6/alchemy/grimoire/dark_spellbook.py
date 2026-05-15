#!/usr/bin/env python3

from .dark_validator import validate_ingredients


def dark_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valideted_result = validate_ingredients(ingredients)
    return f"Spell {spell_name} record: {valideted_result}"
