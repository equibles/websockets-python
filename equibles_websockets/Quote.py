class Quote:
    def __init__(self, ticker: str, price: float, volume: float, timestamp: int):
        self.ticker: str = ticker
        self.price: float = price
        self.volume: float = volume
        self.timestamp: int = timestamp
