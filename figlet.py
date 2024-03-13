import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Usage: python figlet.py [-f <font>]")
    sys.exit(1)

def get_random_font():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    return random.choice(available_fonts)

def main():
    if len(sys.argv) == 1:
        font = get_random_font()
    elif len(sys.argv) == 3 and sys.argv[1] in ('-f', '--font'):
        font = sys.argv[2]
        figlet = Figlet(font=font)
        if font not in figlet.getFonts():
            print(f"Font '{font}' not found.")
            sys.exit(1)
    else:
        print_usage_and_exit()
    user_input = input("Enter text: ")
    figlet = Figlet(font=font)
    rendered_text = figlet.renderText(user_input)
    print(rendered_text)

if __name__ == "__main__":
    main()
