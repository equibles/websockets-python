import logging

from signalrcore.hub_connection_builder import HubConnectionBuilder
from signalrcore.protocol.messagepack_protocol import MessagePackHubProtocol

from .Quote import Quote


class EquiblesWebSocketsClient:
    def __init__(self, api_key, endpoint, tickers, enable_compression = True, debug = False):
        self.debug = debug
        self.tickers = tickers
        self.enable_compression = enable_compression
        self.endpoint = endpoint
        self.api_key = api_key
        self.on_quote_callback = None

        # builds the connection
        connection_builder = HubConnectionBuilder() \
            .with_url("http://websockets.equibles.com/" + self.endpoint) \
            .with_automatic_reconnect({
                "type": "raw",
                "skip_negotiation": True,
                "keep_alive_interval": 10,
                "reconnect_interval": 5,
                "max_attempts": 5
        })
        if self.debug:
            connection_builder = connection_builder.configure_logging(logging.DEBUG)
            
        if self.enable_compression:
            connection_builder = connection_builder.with_hub_protocol(MessagePackHubProtocol())

        self.connection = connection_builder.build()

    def __handle_authentication_result(self, success, error_message):
        if not success:
            print("Error while authenticating: " + error_message)
        else:
            print("Authentication completed with success")
            self.start_listening(self.tickers)

    def __handle_start_listening_result(self, success, error_message):
        if not success:
            print("Error while registering tickers: " + error_message)
        else:
            print("The client is now listening to the server...")

    def __handle_quote(self, data):
        quote = Quote(data["t"], data["p"], data["v"], data["ts"])
        if self.on_quote_callback is not None:
            self.on_quote_callback(quote)

    def __register_listeners(self):
        self.connection.on_open(lambda: self.connection.send("Authentication", [self.api_key]))
        self.connection.on("AuthenticationResult", lambda args: self.__handle_authentication_result(*args))
        self.connection.on("StartListeningResult", lambda args: self.__handle_start_listening_result(*args))
        self.connection.on("Quote", lambda args: self.__handle_quote(*args))

    def connect(self):
        self.__register_listeners()
        self.connection.start()

    def on_quote(self, callback):
        self.on_quote_callback = callback

    def start_listening(self, tickers: list[str]):
        self.connection.send("StartListening", [tickers])

    def stop_listening(self, tickers: list[str]):
        self.connection.send("StopListening", [tickers])

    def disconnect(self):
        self.connection.stop()
