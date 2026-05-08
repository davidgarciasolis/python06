#!/usr/bin/python3
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()

    valid = False
    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in lower_ingredients:
            valid = True
            break

    if valid:
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
