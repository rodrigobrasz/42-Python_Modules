#! /usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        s = input("Enter new coordinates in float format: ")
        splited = s.split(",")
        length = len(splited)
        try:
            if length != 3:
                print("Ivalide syntax. Please try again.")
                continue

            param = splited[0]
            x = float(splited[0].strip())
            param = splited[1]
            y = float(splited[1].strip())
            param = splited[2]
            z = float(splited[2].strip())

        except ValueError as e:
            print(f"Error parameter ({param}) : {e}")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinates system ===")

    print("\nGet the first set of Coordinates:")
    print("Enter new cordinates as floats format 'x, y, z':")
    pos1 = get_player_pos()
    print(f"First set: X = {pos1[0]}, Y = {pos1[1]}, Z = {pos1[2]}")
    center_distance = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    center_distance = round(center_distance, 4)
    print(f"{center_distance}")

    print("\nGot the second set of Coordinates:")
    print("Enter new cordinates as floats format 'x, y, z':")
    pos2 = get_player_pos()
    distance_sets = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2
                              + (pos2[2] - pos1[2])**2)
    distance_sets = round(distance_sets, 4)
    print(f"Distance between the 2 sets of coordinates: {distance_sets}")


if __name__ == "__main__":
    main()
