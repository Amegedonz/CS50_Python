def main():
    greeting = input("Greeting: ")

    WOWS = greeting.strip()
    ModGreet = WOWS.lower()

    if ModGreet == "hello":
        print("$0")
    elif ModGreet.startswith('h'):
        print("$20")
    else:
        print("$100")


main()