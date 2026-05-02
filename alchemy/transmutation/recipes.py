#!/usr/bin/python3
from alchemy import elements
from .. import potions


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '"
            f"{elements.create_air()}' and '"
            f"{potions.strength_potion()}' mixed with '"
            f"{potions.create_fire()}'")
