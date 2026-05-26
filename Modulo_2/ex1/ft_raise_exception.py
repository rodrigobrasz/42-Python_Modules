#!/usr/bin/env python3

class TemperatureError(Exception):
    pass


def input_temperature(temp_str):
    try:
        temp_str = int(temp_str)
    except ValueError:
        raise TemperatureError("Caught input_temperature error: invalid "
                               "literal"
                               " for int() with base 10:")

    if temp_str > 40:
        raise TemperatureError(f"Caught input_temperature error: {temp_str}"
                               " is too hot for plants (max 40°C)")

    elif temp_str < 0:
        raise TemperatureError(f"Caught input_temperature error: {temp_str}"
                               " is too cold for plants (min 0°C)")

    return temp_str


def test_temperature():
    input_data_1 = 400
    input_data_2 = -100
    input_data_3 = "abc"

    print("=== Garden Temperature Checker ===\n")
    print(f"Input data is ({input_data_1})")
    try:
        result_1 = input_temperature(input_data_1)
        print(input_temperature(result_1))
    except TemperatureError as e:
        print(e)

    print()

#   dmalsmdaslkdkmlas
    print(f"Input data is ({input_data_2})")
    try:
        result_2 = input_temperature(input_data_2)
        print(input_temperature(result_2))
    except TemperatureError as e:
        print(e)

    print()

    print(f"Input data is ({input_data_3})")
    try:
        print(input_temperature(input_data_3))
    except TemperatureError as e:
        print(e)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
