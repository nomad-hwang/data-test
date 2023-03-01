import os
import unittest
from datetime import datetime

import polars as pl

pl.Series

PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_data")
PATH = os.path.join(PATH, "BTCUSDT-trades-2023-02-26.csv")


class TestLoadTickData(unittest.TestCase):
    def setUp(self):
        # trade Id	price	qty	quoteQty	time	isBuyerMaker	isBestMatch
        self.df = pl.read_csv(
            PATH,
            has_header=False,
            columns=[1, 2, 4],
            new_columns=["price", "qty", "time"],
            # dtypes={"time": pl.Datetime(time_unit="ms"), "price": pl.Float64, "qty": pl.Float64},
            dtypes={"time": pl.Time, "price": pl.Float64, "qty": pl.Float64},
            # try_parse_dates=True,
        )

        # self.df = self.df.upsample
        print(self.df)
        print(self.df.shape)
        print(self.df.schema)

    def test_load_tick_data(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
