""" Module that provides some utilities to format stdout text"""
import random

RESET_COLOR = "\033[0m"

def random_color()-> None:
    """
    Generate random RGB values
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\033[38;2;{r};{g};{b}m"

def color_line(text)-> None:
    """
    Paint a text line
    :param: text: line of text to paint
    """
    color = random_color()
    return f"{color}{text}{RESET_COLOR}"