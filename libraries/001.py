import sys
import requests
import json

bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin = bitcoin.json()
bitcoin = float(bitcoin["bpi"]["USD"]["rate"].replace(",", ""))

try:
    amount = float(sys.argv[1])
except:
    print("missing command-line argument")
else:
    print(f"${(amount * bitcoin):,.2f}")