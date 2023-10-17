def main():
    print(value(input("Greeting: ")))


def value(greeting):
    if (greeting.lower()).startswith("h"):
        if (greeting.lower()).startswith("hello"):
            return ("$0")
        
        return ("$20")
    
    else:
        return ("$100")



if __name__ == "__main__":
    main()