def main():
    while True:
        percentage = convert(input("Fraction: "))
        if percentage:
            print(gauge(percentage))
            break



def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        return (x/y*100)


    except (ValueError, ZeroDivisionError):
        return False
    


def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"
    
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()