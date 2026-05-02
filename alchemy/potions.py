#!/usr/bin/python3
from alchemy.elements import create_air as create_air, create_earth as create_earth
from elements import create_fire as create_fire, create_water as create_water


def healing_potion() -> str:
    return (f"Healing potion brewed with '"
            f"{create_earth()}' y '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with '"
            f"{create_fire()}' y '{create_water()}'")
