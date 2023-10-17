def main():
    removeVowels(getInput())

def getInput():
    while True:
        try:
            return str(input("Input: "))
        
        except TypeError:
            pass

def removeVowels(toChange):
    vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    print('Output: ', end='')
    for i in toChange:
        if i not in vowles:
            print(i, end = '')
    print()


if __name__ == "__main__":
    main()