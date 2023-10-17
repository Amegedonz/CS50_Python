import inflect

def main():
    p = inflect.engine()
    print(f"Adieu, Adieu to {p.join(createList(),final_sep='')}")


def createList():
    nameList = []
    while True:
        try: 
            nameList.append(input("Name: "))

        except EOFError:
            return nameList


main()