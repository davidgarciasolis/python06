#!/usr/bin/python3
from alchemy import elements
from .. import potions


def lead_to_gold() -> None:
	return (f"Recipe transmuting Lead to Gold: brew '{elements.create_air()}' and '{potions.strength_potion()}' mixed with '{potions.create_fire()}'")