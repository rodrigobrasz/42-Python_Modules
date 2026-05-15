#!/usr/bin/env python3

import sys
import typing


def read_file() -> None:
    print("=== Cyber Archives Recovery ===\n")
    file = sys.argv[1]
    oppened: typing.Optional[typing.TextIO] = None
    print(f"Acessing file: '{file}'\n")

    try:
        oppened = open(file, "r")
        print("---")
        print(oppened.read())
        print("---")
    except OSError as e:
        print(f"Error oppening file {oppened}: {e}")
        return
    finally:
        if oppened is not None:
            oppened.close()
        print(f"\nFile '{file}' Closed.")


def main() -> None:
    length = len(sys.argv)
    if length != 2:
        print(f"Usage: python3 {sys.argv[0]} <file.txt>")
        return
    read_file()


if __name__ == "__main__":
    main()
