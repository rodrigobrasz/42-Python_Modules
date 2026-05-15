#!/usr/bin/env python3

def input_temperature(temp_str):
    try:
        return int(temp_str)
    except ValueError:
        return None


def test_temperature() -> None:

    valid_input = "25"
    invalid_input = "abc"

    first_result = input_temperature(valid_input)
    second_input = input_temperature(invalid_input)
    print("=== Garden Temperature ===\n")

    print(f"Input data is '{valid_input}'")
    if first_result is not None:
        print(f"Temperature is now {first_result}°C\n")

    print(f"Input data is '{invalid_input}'")
    if second_input is None:
        print(
            f"Caught input_temperature error: invalid literal"
            f" for int() with base 10: '{invalid_input}'\n"
              )

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
