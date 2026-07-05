from typing import Any

def garden_oerations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("aaa")
    elif operation_number == 3:
        value: Any = 1
        value + "a"
    else:
        print("Operation completed successfully\n")


def test_error_types() -> None:
    for i in range(0, 5):
        try:
            garden_oerations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
