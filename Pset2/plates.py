def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # plate = tuple(s)
    # if len(plate) > 6 or len(plate) < 2:
    #     return False
    
    # if plate[-1].isalpha():
    #     for i in plate:
    #         if i.isnumeric():
    #             return False
    
    # if plate[0] == '0':
    #     return False

    # if plate[0].isalpha() and plate[1].isalpha():
    #     print("Yes")


    for i in s:
        for postition in len(range(s)):
            print(list(zip(i, postition)))

    # for num in len(s):
    #     for letter in s:
    #         if 


main()


# “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    # “No periods, spaces, or punctuation marks are allowed.”
