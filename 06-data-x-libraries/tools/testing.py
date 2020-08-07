import time
import random
from tools.finance import TickerInfo



def test_finance_TickerInfo():
    x = TickerInfo()
    def testing():
        t = time.perf_counter()
        ticker = "GOOG" if random.random() > 0.5 else "NFLX"
        x.get_current_price(ticker)
        print("Retrieved",ticker,"information in", time.perf_counter() - t, "seconds")

    for _ in range(100):
        testing()




test_finance_TickerInfo()