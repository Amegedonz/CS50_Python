def main():
    camel = input("camelCase: ")
    camelToSnake(camel)


def camelToSnake(camel):
    snake = []
    for i in range(len(camel)):
        if camel[i].isupper():
            snake = camel[:i] + f"_{camel[i].lower()}" + camel[i+1:]
            camel = snake
    print(f"snake_case: {snake}")


            

main()