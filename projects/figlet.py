import sys
from pyfiglet import Figlet
import random as rd
figlet = Figlet()

try:
    if len(sys.argv) > 2 and sys.argv[1] == "-f" or "-- font":
        figlet.setFont(font=sys.argv[2])

    else:
        print("Invalid usage")
        sys.exit()

except IndexError:
    figlet.setFont(font=rd.choice(figlet.getFonts()))
   


text = input("input: ")
print(figlet.renderText(text))