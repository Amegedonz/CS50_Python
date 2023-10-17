#answering the question with 42 alphanumerically case insensititivel

def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")

    x = x.replace(" ","")
    if x.isalpha():
        x = x.lower()

    match x:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "fortytwo":
            print("Yes")
        case _:
            print("No")

main()