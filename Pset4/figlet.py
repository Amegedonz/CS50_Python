import sys
import random
from pyfiglet import Figlet
figlet = Figlet()


def main():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                outputGeneration(getInput(), sys.argv[2])
                sys.exit()

        sys.exit("Invalide usage")

    except IndexError:
        outputGeneration(getInput(), random.choice(figlet.getFonts()))
       
    
def getInput():
    return input("Input: ")


def outputGeneration(text, fontName):
    figlet.setFont(font=fontName)
    print("Output: ")
    print(figlet.renderText(text))
    

main()