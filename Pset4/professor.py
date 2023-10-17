import random
possibleLevels = [1,2,3]

def main():
    level = get_level()
    correctCount = 0
    for problems in range(10):
        num = []
        answer = 0
        wrongCount = 0
        for number in range(2):
            ranNum = generate_integer(level) 
            num.append(ranNum)
            answer += ranNum
        while wrongCount < 3:
            try:
                if int(input(f"{num[0]} + {num[1]} = ")) == answer:
                    correctCount += 1
                    break

                else:
                    raise ValueError
                
            except ValueError:
                print("EEE")
                wrongCount += 1
                if wrongCount == 3:
                    print(f"{num[0]} + {num[1]} = {answer}")
                pass
    
    print(f"Number of correct answers = {correctCount}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in possibleLevels:
                return level
        
        except (ValueError, TypeError):
            pass
    


def generate_integer(level):
    return(random.randint(1, 10**(level)))


if __name__ == "__main__":
    main()