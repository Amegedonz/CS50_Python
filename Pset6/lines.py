import sys

def main():
    if checkCommandLine():
        print(readLine(sys.argv[1]))


def checkCommandLine():
    try:
        if sys.argv[1].endswith(".py"):
            if sys.argv[2]:
                raise IndexError

        sys.exit("Not a python file")

    except IndexError:
        if len(sys.argv) < 1:
            sys.exit("Too few command-line arguments")
        
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        else:
            return True


def readLine(doc):
    lineCount = 0
    try:
        with open(doc, 'r') as file:
            for lines in file.readlines():
                filteredLine = lines.lstrip()
                if filteredLine[0].isascii():
                    lineCount += 1

                if filteredLine.startswith("#"):
                    lineCount -= 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return(lineCount)


if __name__ == "__main__":
    main()