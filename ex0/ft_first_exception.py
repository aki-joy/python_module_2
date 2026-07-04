def input_temperature(temp_str: str) -> int:
    temp_int = temp_str
    return temp_int


def test_temperature() -> None:

    test_temps = ["25", "abc"]
    print("=== Garden Temperature ===")
    for test_temp in test_temps:

        print(f"Input data is '{test_temp}'")

        try:
            temp = input_temperature(test_temp)
            print(f"Temperature is now {temp}℃")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")
