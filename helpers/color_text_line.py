import random

reset = "\033[0m"

def random_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\033[38;2;{r};{g};{b}m"

def color_line(text):
    # Color line
    color = random_color()
    return f"{color}{text}{reset}"