def main():
    accepted = [5, 10, 25]
    due = 50
    while due > 0:
        due = getCoin(accepted, due)
        print(f"Amount Due = {due}")

    print(f"Change Owed = {due}")

def getCoin(value, due):
    while True:
        coinInput = int(input("Inesert Coin: "))
        if coinInput in value:
            return (due - coinInput)
        else:
            return due




main()