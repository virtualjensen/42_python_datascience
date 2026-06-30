import sys

def main():
    """
        This program takes a single string argument and displays the sums of its 
        upper-case characters, 
        lower-case characters, 
        punctuation characters, 
        digits, 
        and spaces. 

        If none or nothing is provided, the user is prompted to provide a string. 
        If more than one argument is provided to the program, an AssertionError is raised. 
    """
    if len(sys.argv) == 1:
        user_input = input("Please provide a string: ")
    else:
        assert len(sys.argv) == 2, "more than one argument is provided"
        user_input = sys.argv[1]

    upper_count = sum(1 for char in user_input if char.isupper())
    lower_count = sum(1 for char in user_input if char.islower())
    punctuation_count = sum(1 for char in user_input if not char.isalnum() and not char.isspace())
    digit_count = sum(1 for char in user_input if char.isdigit())
    space_count = sum(1 for char in user_input if char.isspace())

    print(f"The text contains {len(user_input)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

if __name__ == "__main__":
    main()

# This time you have to make a real autonomous program, with a main, which takes
# a single string argument and displays the sums of its upper-case characters, lower-case
# characters, punctuation characters, digits, and spaces.
# • If none or nothing is provided, the user is prompted to provide a string.
# • If more than one argument is provided to the program, print an AssertionError.
# Expected outputs:
# $>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
# compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 7 punctuation marks
# 26 spaces
# 15 digits