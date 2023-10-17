def main():
    time = convert(input("Enter time here: "))
    if time >= 7 and time <= 8:
        print("Breakfast time")
    
    if time >= 12 and time <= 13:
        print("Lunch time")

    if time >= 18 and time <= 19:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) /60
    hours = int(hours)
    return (hours+minutes)

if __name__ == "__main__":
    main()