####################################
#                                  #
#    Algorand to USD Converter     #
#                                  #
####################################

import requests

### Prompt user for input, and remove comma if entered

algo_amount = input("Enter an amount in $ALGO: ")
algo_amount = float(algo_amount.replace(",", ""))

### Setup API variables & parameters

url = "https://api.coingecko.com/api/v3/simple/price"

parameters = {
    "ids": "algorand",
    "vs_currencies": "usd"
}

response = requests.get(url, params=parameters)

### Calculate, format, and print USD price

if response.status_code == 200:
    data = response.json()
    conversion = round(algo_amount * float(data["algorand"]["usd"]), 2)
    conversion_formatted = "{:,}".format(conversion) # Insert comma for thousands
    algo_amount_formatted = "{:,.2f}".format(algo_amount) # Insert comma for thousands, round to two decimal places
    print(f"{algo_amount_formatted} $ALGO is currently equal to ${conversion_formatted} USD.")

else:
    print("ERROR: Unable to get price data.")
