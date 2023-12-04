"""
input_reader module with input validation
"""

def read_float(text_to_display):
    """
    read a float from the console
    :param text_to_display: Text to display
    :return: float
    """
    while True:
        try:
            num = float(input(text_to_display))
        except ValueError:
            print("Please, enter a real number!")
            continue
        else:
            return num


def read_int(text_to_display):
    """
    read an int from the console
    :param text_to_display:
    :return: int
    """
    while True:
        try:
            num = int(input(text_to_display))
        except ValueError:
            print("Please, enter a valid whole number!")
            continue
        else:
            return num