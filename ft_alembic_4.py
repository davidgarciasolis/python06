#!/usr/bin/python3
import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: Air element created")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(f"Testing create_air: {alchemy.create_earth()}")  # type: ignore[attr-defined]


if __name__ == "__main__":
    main()
