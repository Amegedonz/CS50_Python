menu =  {
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
    sum = 0
    order = 1
    while order != "":
        order = getOrder()
        if order in menu:
            sum += menu[order]
            print(f"Total: ${sum:.2f}")

def getOrder():
    return input("Item: ").title()
  


main()