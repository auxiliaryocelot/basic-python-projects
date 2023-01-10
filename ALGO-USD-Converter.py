####################################
#                                  #
#    Algorand to USD Converter     #
#                                  #
####################################

import requests
import datetime

# Prompt user for input, and remove comma if entered
algo_amount = float(input("Enter an amount in $ALGO: ").replace(",", ""))

# Setup API variables & parameters
url = "https://api.coingecko.com/api/v3/simple/price"

parameters = {
    "ids": "algorand",
    "vs_currencies": "usd"
}

response = requests.get(url, params=parameters)

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string
time_string = now.strftime("%I:%M%p on %A, %B %d")

# Calculate, format, and print prices, along with date/time
if response.status_code == 200:
    data = response.json()
    current_price = round(float(data["algorand"]["usd"]), 3)
    conversion = algo_amount * current_price
    conversion_formatted = "{:,.2f}".format(conversion) # Insert comma for thousands, round to two decimal places
    algo_amount_formatted = "{:,.2f}".format(algo_amount) # Insert comma for thousands, round to two decimal places
    
    print(f"{algo_amount_formatted} $ALGO is currently equal to ${conversion_formatted} USD. $ALGO is currently ${current_price} as of {time_string} as per CoinGecko price information")

else:
    print("ERROR: Unable to get price data.")

# Probably not the best way to keep the program from
# immediately closing, but I'm open to suggestions!

input("")