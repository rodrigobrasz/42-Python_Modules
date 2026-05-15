#!/usr/bin/env python3

def garden_operations(operation_num: int) -> None:
    if operation_num == 0:
        int("abc")
    elif operation_num == 1:
        10 / 0
    elif operation_num == 2:
        open("file.txt")
    elif operation_num == 3:
        "abc" + 1


def test_error_types() -> None:
    print("=== Garden Types Demo ===")
    i = 0
    while i < 4:
        print(f"Testing {i}")
        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught: ", e)
        except ZeroDivisionError as e:
            print("Caught: ", e)
        except FileNotFoundError as e:
            print("Caught: ", e)
        except TypeError as e:
            print("Caught: ", e)
        i += 1
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
