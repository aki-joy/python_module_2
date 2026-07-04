def garden_oerations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        result = 10 / 0
    if operation_number == 2:
        open("aaa")
    if operation_number == 3:
        result = 1 + "a"
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range (0, 4):
        try:
            garden_oerations(i)
        except ValueError as e:
            print


if __name__ == "__main__":
    test_error_types()