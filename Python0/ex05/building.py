from string import punctuation
from sys import argv


def count(user_input: str):
    """
    Function: count
    This function counts and prints a sum of each type to character,
    it has a dictionary where the key are the char types
    and the values are the count
    """

    if not len(argv) < 2 or len(user_input) == 0:
        text: str = ""
    else:
        text = user_input or argv[1]
    counts = {
        'upper': sum(1 for char in text if char.isupper()),
        'lower': sum(1 for char in text if char.islower()),
        'punctuation': sum(1 for char in text if not char.isalnum()
                           and not char.isspace()),
        'spaces': sum(1 for char in text if char.isspace()),
        'digits': sum(1 for char in text if char.isdigit()),
    }
    print(f"The text contains {len(text) or 0} characters:")
    for char in counts.keys():
        if char == "upper" or char == "lower":
            print(f"{counts[char]} {char} letters")
        elif char == "punctuation":
            print(f"{counts[char]} {char} marks")
        else:
            print(f"{counts[char]} {char}")


def main():
    """
    Function:Main
    In our main we are checking if arg count is less or equal than 2
    if this assert fails, the program can't continue.
    If this assert checks, and if arg coung is 1 (no text provided),
    the program ask for the text to process.
    """

    try:
        assert (len(argv) <= 2)
    except AssertionError:
        print("AssertionError: more than one argument is provided")
        exit(1)
    user_input: str = ""
    if len(argv) == 1:
        try:
            user_input = input("What is the text to count?\n")
        except EOFError:
            print("\nEOF detected. Exiting")
            exit(0)

    count(user_input)


if __name__ == "__main__":
    main()
