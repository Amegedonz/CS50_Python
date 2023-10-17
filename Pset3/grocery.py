Groceries = {}

#Main loop to run functions
def main():
    while True:
        try:
            item = getItem()
            listGroc(item)
        
        
        except EOFError:
            for key in Groceries:
                print(Groceries[key], key)
            return 0


#Input function (strips whitespace and converts into uppercase)
def getItem():
    return((input().strip()).upper())
    
#Adds/ Edits the dict based on inputs
def listGroc(item):
    if item in Groceries:
        Groceries[item] = Groceries[item] + 1
    else:
        Groceries[item] = 1


main()