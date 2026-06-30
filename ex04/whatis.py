import sys

# If no argument is given, print nothing
if len(sys.argv) == 1:
    sys.exit()

try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    number = int(sys.argv[1])

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("AssertionError: argument is not an integer")