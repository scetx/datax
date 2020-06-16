import time
from tools.finance import TickerInfo



def test_finance_TickerInfo(ticker="GOOG"):
    x = TickerInfo()
    def testing():
        t = time.perf_counter()
        x.get_current_price(ticker)
        print("Retrieved stock information in ", time.perf_counter() - t, "seconds")

    for _ in range(100):
        testing()



test_finance_TickerInfo()