#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    l_ingredientes = ingredients.lower()
    for x in allowed:
        if x.lower() in l_ingredientes:
            return f"[{ingredients}] is Valid"
    return f"{ingredients}is Invalid"
