#!/usr/bin/python3
from alchemy import potions

def main() -> None:
	print("=== Distillation 0 ===")
	print("Direct access to alchemy/potions.py")
	print(f"Testing strength_potion: {potions.healing_potion()}")
	print(f"Testing healing_potion: {potions.healing_potion()}")


if __name__ == "__main__":
	main()