Menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    totalCost = 0
    while True:
        try:
            menuItem = getItem("Item: ")
            totalCost = totalCost + Menu[menuItem]
            printTotal(totalCost)
    
        except KeyError:
            print()
            return 0


def getItem(prompt):
    while True:
        try:
            itemInput = input(prompt)
            formatedInput = itemInput.title()
            if formatedInput in Menu:
                return(formatedInput)
            else:
                pass
    
        except EOFError:
            return 0


def printTotal(total):
    formatTotal = "{:.2f}".format(float(total))
    print("Total: $", end='')
    print(formatTotal)


main()