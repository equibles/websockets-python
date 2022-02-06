from equibles_websockets import EquiblesWebSocketsClient, endpoints, Quote

client = EquiblesWebSocketsClient(api_key="MY_API_KEY", endpoint=endpoints.CRYPTOS, tickers=["BTC", "ETH"], debug=False)
client.connect()


def do_stuff(quote: Quote):
    print(quote.ticker + ": " + str(quote.price))


client.on_quote(do_stuff)

input("Press enter to exit: ")
print("Exited.")
