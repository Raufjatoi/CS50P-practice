import sys
from pyfiglet import Figlet

figlet = Figlet()
font_list = getFonts()
if len(sys.argv) != 3:
    r = input('Input: ')
    print(figlet.renderText(r))
elif sys.argv[1] in ('-f', '--font'):
    font = sys.argv[2]
    if sys.argv[2] in list:
        figlet.setFont(font)
    r = input('Input: ')
    print(figlet.renderText(r))
