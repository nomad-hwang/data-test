import polars as pl

from engine.pattern.pubsub import Publisher


class DataPool(Publisher):
    """
    Source: Redis, File, ...
    Data: OHLCV, Indicator, ...(Columnar data)
    """

    """DataPool is an abstract class for data pool
    - It's purpose is to store data in shared memory for the worker
    - It does the following:
        - Fetches and caches subscribed/requested data from data source and notifies the subscriber
        - Worker saves the data to the data pool and notifies the subscriber
    - Worker can do the following:
        - Subscribe with key
        - Get data
        - Append data
    - Data keys:
        - 'EXCHANGE:SYMBOL'
    """

    def get(self, key: str, type: str, limit: int = 10) -> pl.DataFrame:
        pass

    def append(self, key: str, type: str, data: pl.DataFrame) -> None:
        pass
