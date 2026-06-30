import sys
from ft_filter import ft_filter


def is_integer(value):
    """Return True if value can be converted to an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    """Filter words from a string that are longer than a given number."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        string = sys.argv[1]
        number = sys.argv[2]

        if not isinstance(string, str) or not is_integer(number):
            raise AssertionError("the arguments are bad")

        n = int(number)

        words = string.split("")

        result = [
            word for word in ft_filter(lambda word: len(word) > n, words)
        ]

        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()