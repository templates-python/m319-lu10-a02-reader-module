"""Main program that reads a real number and a whole number from the console."""


def main():
    # do something
    """
    Reads a float and an int and prints them.
    """
    in_float = read_float('Please enter a real number> ')
    in_int = read_int('Please enter a whole number> ')

    print(in_float)
    print(in_int)


if __name__ == '__main__':
    main()
