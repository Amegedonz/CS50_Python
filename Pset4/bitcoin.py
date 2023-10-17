import sys
import requests

def main():
    try:
        inputNum = float(sys.argv[1])
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoinRate = r.json()["bpi"]["USD"]["rate"].replace(',', '')
        totalCost = inputNum * float(bitcoinRate)
        print(f"{totalCost:,.4f}")
        sys.exit

    except ValueError:
        print("Command-Line argument is not a number")
        sys.exit()

    except IndexError:
        print("Missing Command-line argument")
        sys.exit

    except requests.RequestException:
        print("Issue with API")
        sys.exit



if __name__ == "__main__":
    main()
