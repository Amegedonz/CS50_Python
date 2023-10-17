def main():
    print(shorten(input("Enter word here: ")))


def shorten(word):
    editedWord = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i.lower() not in vowels:
            editedWord = editedWord + i
    return editedWord


if __name__ == "__main__":
    main()