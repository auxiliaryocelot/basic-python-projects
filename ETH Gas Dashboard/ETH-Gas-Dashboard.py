####################################
#                                  #
#        ETH Gas Dashboard         #
#                                  #
####################################

import requests
import datetime
from config import key

# Establish API URL's & JSON Variables
gas_oracle_url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={key}"
eth_price_url = f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={key}"
gas_price_data = requests.get(gas_oracle_url).json()
eth_price_data = requests.get(eth_price_url).json()

# Establish variables for different gas tiers
safe = float(gas_price_data['result']['SafeGasPrice'])
proposed = float(gas_price_data['result']['ProposeGasPrice'])
fast = float(gas_price_data['result']['FastGasPrice'])

# Establish and format variable for ETH price
eth_current = eth_price_data['result']['ethusd']
eth_format = "{:,.2f}".format(float(eth_current))

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
time_string = now.strftime("%I:%M%p on %A, %B %d")

# Print Dashboard
print("")
print(f"Current $ETH Gas Prices as of {time_string}:")
print("----------")
print(f"Safe Price: {safe} Gwei")
print(f"Proposed Price: {proposed} Gwei")
print(f"Fast Price: {fast} Gwei")
print("----------")
print(f"Current $ETH price is ${eth_format}")

# Probably not the best way to keep the program from
# immediately closing, but I'm open to suggestions!
input("")
