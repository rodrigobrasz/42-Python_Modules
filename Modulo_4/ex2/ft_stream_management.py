#!/usr/bin/env python3

import sys
import typing


def stderr_message(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")


def read_file() -> None:
    print("=== Cyber Archives Recovery & Preservation ===\n")
    file = sys.argv[1]
    opened: typing.TextIO | None = None
    print(f"Accessing file: '{file}'\n")

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
        stderr_message(f"Error opening file '{file}': {e}")
        return
    finally:
        if opened is not None:
            opened.close()
            print(f"File '{file}' closed.")

    sys.stdout.write("Enter new file name (or emppty): ")
    sys.stdout.flush()

#   Lê/Retira a \n do stdin e salva em "new_name":
    new_name = sys.stdin.readline()
    new_name = new_name.strip("\n")
    if new_name == "":
        print("No saving name provided. Please try again")
        return

    print(f"Saving a new data for {new_name}")
    try:
        new_file_name = open(new_name, "w")
    except OSError as e:
        stderr_message(f"Error opening file '{new_name}': {e}")
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
