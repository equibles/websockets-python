# Equibles WebSockets live quotes for Python

## Requirements.
Python 3.4+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/equibles/websockets-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/equibles/cryptos-python.git`)

Then import the package:
```python
import equibles_websockets 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from equibles_websockets import EquiblesWebSocketsClient, endpoints, Quote

# Create a websockets client. Replace the string "MY_API_KEY" with your own API key. 
# Use the "tickers" argument to choose the tickers you want to listen to. You can listen to as many as you want. 
client = EquiblesWebSocketsClient(api_key="MY_API_KEY", endpoint=endpoints.CRYPTOS, tickers=["BTC", "ETH"], debug=False)
client.connect()

def do_stuff(quote: Quote):
    print(quote.ticker + ": " + str(quote.price))

client.on_quote(do_stuff)

input("Press enter to exit: ")
print("Exited.")
```


## Author
[Equibles](https://www.equibles.com)\
equibles@gmail.com