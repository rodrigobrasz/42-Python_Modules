#!/usr/bin/env python3

import sys
import typing


def read_file() -> None:
    print("=== Cyber Archives Recovery & Preservation ===\n")
    file = sys.argv[1]
    opened: typing.TextIO | None = None
    print(f"Acessing file: '{file}'\n")

    try:

        opened = open(file, "r")
        content = opened.read()
        print("---")
        print(content, end="")
        print("\n---")

        new_content = ""
        for line in content.splitlines(True):
            if line.endswith("\n"):
                new_content += line[:-1] + "#\n"
            else:
                new_content += line + "#"
        print("\nTransform Data:\n")
        print("---")
        print(new_content)
        print("---")

    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    finally:
        if opened is not None:
            opened.close()
            print(f"File '{file}' closed.")

    new_name = input("Enter new file name: ")
    if new_name == "":
        print("No saving name provided. Please try again")
        return

    print(f"Saving a new data for {new_name}")
    try:
        new_file_name = open(new_name, "w")
    except OSError as e:
        print(f"Error opening file '{new_name}': {e}")
        print("Data not saved.")
        return

    try:
        new_file_name.write(new_content)
    finally:
        new_file_name.close()
        print(f"Data saved to '{new_name}'")


def main() -> None:
    length = len(sys.argv)
    if length != 2:
        print(f"Usage: python3 {sys.argv[0]} <file.txt>")
        return
    read_file()


if __name__ == "__main__":
    main()
