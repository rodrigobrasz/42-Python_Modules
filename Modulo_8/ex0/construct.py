#!/usr/bin/env python3

import sys
import os
import site


def venv_matrix() -> bool:
    return sys.prefix != sys.base_prefix


def venv_name() -> str:
    return os.path.basename(os.getenv("VIRTUAL_ENV"))


def main() -> None:
    check = venv_matrix()
    cur = sys.executable
    if not check:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current python {cur}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")

        print("\nThen run this program again.")
        return

    print("MATRIX STATUS: Wellcome to the construct\n")

    print(f"Current Pythom = {cur}")
    print(f"Virtual Environment = {venv_name()}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    pack = site.getsitepackages()
    print("Package installation path:")
    print(f"{pack[0]}")


if __name__ == "__main__":
    main()
