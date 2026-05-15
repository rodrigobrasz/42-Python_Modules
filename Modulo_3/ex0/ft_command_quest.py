#!/usr/bin/env python3

import sys


def arg_counter(arg: list) -> None:
    lenght = len(arg) - 1
    if lenght == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received {lenght}")
    i = 1
    while i <= lenght:
        print(f"Agument {i}: {arg[i]}")
        i += 1


def main() -> None:
    n = len(sys.argv)
    print("=== Comand Quest ===")
    print("Program Name:", sys.argv[0])

    arg_counter(sys.argv)

    print(f"Total arguments: {n}")


if __name__ == "__main__":
    main()
