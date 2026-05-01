#!/usr/bin/python3
import alchemy

def main() -> None:
	print("=== Distillation 1 ===")
	print("Using: 'import alchemy' structure to access potions")
	print(f"Testing strength_potion: {alchemy.healing_potion()}")
	print(f"Testing healing_potion: {alchemy.strength_potion()}")


if __name__ == "__main__":
	main()