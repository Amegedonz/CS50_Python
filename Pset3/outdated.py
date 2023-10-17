month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


#runs input as long as MM/DD/YYYY format or month in alpha
def main():
    dateInput = getDate()
    datePrint(dateInput[0], dateInput[1])


#function to collect and check validity of input
#returns date as a list
def getDate():
    while True:
        dateInt = (input("Date: ").split("/"))
        dateInt[0] = dateInt[0].title()
        print(dateInt)

        if dateInt[0].isalpha():
            dateMonth = monthToNum(dateInt[0])
        
        else:
            dateMonth = int(dateInt[0])

        try:
            if int(dateInt[1]) < 32 and dateMonth < 13:
                return(dateInt, dateMonth)
                
            else:
                pass

        except (TypeError, IndexError, ValueError):
            pass


#function to convert alpha month to month number
def monthToNum(monthInput):
    for x in range(len(month)):
        if month[x] == monthInput:
            return x + 1


#prints new date
def datePrint(date, monthNum):
    print(f"{date[2]}-{monthNum}-{date[1]}")


main()