#!/usr/bin/python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients = light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()

    valid = False
    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in lower_ingredients:
            valid = True
            break

    if valid:
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
