def main():
    print("Hello, world!")


def test_string_reverse():
    assert "hello"[::-1] == "olleh"
    print("Test passed")

if __name__ == "__main__":
    test_string_reverse()
