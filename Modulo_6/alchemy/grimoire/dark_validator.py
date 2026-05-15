#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    for ingredient in allowed:
        if ingredient.lower() in ingredients_lower:
            return f"[{ingredients}] is VALID"

    return f"[{ingredients}] is INVALID"
