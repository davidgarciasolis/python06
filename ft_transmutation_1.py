#!/usr/bin/python3
from alchemy.transmutation import recipes


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()
