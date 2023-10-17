import random

def main():
    level = intCheck("Level: ")
    n = random.randint(1, level)
    nCheck(n)
        


def intCheck(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level


        except ValueError:
            pass


def nCheck(n):
    while True:
        guess = intCheck("Guess: ")
        if n > guess:
            print("Too Small!")

        elif n < guess:
            print("Too Large!")

        else:
            print("Just Right!")
            return 0

main()