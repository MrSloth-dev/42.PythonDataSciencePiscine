from sys import argv


def count(user_input: str):
    text: str = user_input or argv[1]
    counts = {
        'upper': sum(1 for char in text if char.isupper()),
        'lower': sum(1 for char in text if char.islower()),
        'spaces': sum(1 for char in text if char.isspace()),
        'digits': sum(1 for char in text if char.isdigit()),
        'punctuation': sum(1 for char in text if not char.isalnum()
                           and not char.isspace()),
    }
    print(f"The text contains {len(text) or 0} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
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
