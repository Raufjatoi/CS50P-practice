import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except (requests.RequestException, KeyError, ValueError):
        print("Failed to retrieve Bitcoin price.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Number of bitcoins must be a valid number.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price

    print(f"Cost of {bitcoins:,.4f} Bitcoins: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
