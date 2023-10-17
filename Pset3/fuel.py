def main():
    fraction = getFraction("Fraction: ")
    outputFraction(fraction)
    

#fucntion to obtain and return fraction in seperate int values
def getFraction(prompt):
    while True:
        try:
            inputFraction = input(prompt)
            F = inputFraction.split('/')
            if int(F[0]) <= int(F[1]):
                return(int(F[0]), int(F[1]))
        
        except (ValueError, ZeroDivisionError, IndexError):
            pass

#function to calculate and print results
def outputFraction(fraction):
    fractionPercentage = round(int(fraction[0])/ int(fraction[1]) * 100)
    match fractionPercentage:
        case 1 | 0:
            print("E")
        
        case 100 | 99:
            print("F")

        case _:
            print(fractionPercentage, end='')
            print('%')


main()