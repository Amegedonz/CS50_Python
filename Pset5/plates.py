def main():
    if is_valid(input("Enter plate: ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)< 2 or len(s) > 6:
        return False
    
    if s[0].isnumeric() or s[1].isnumeric():
        return False

    numEnd = 2
    for i in range(len(s)):
        if s[i].isalnum():
            if s[i].isnumeric():
                numEnd = 0
            
            if numEnd == 0:
                if s[i].isalpha():
                    numEnd = 1
        
        else:
            return False
        
    if numEnd == 1:
        return False
    
    return True

if __name__ == "__main__":
    main()