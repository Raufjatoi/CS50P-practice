import sys
from pyfiglet import Figlet

figlet = Figlet() 

if len(sys.argv) != 3:
    r = input('Input: ')
    print(figlet.renderText(r))
elif sys.argv[1] in ('-f', '--font'):
    font = sys.argv[2]
    figlet.getFonts()
    figlet.setFont(font)
    r = input('Input: ')
    print(figlet.renderText(r))
else:
    sys.exit('Error: Invalid argument')
