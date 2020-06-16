import threading
import requests
import json
import datetime
import time

class TickerInfo:
    def __init__(self):
        self.memoized_scraped_data = {}
        self.info_keys = {}


    def ____core_parse_helper(self, ticker):
        query_url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&" \
                    "modules=" \
                    "summaryProfile%2C" \
                    "financialData%2C" \
                    "recommendationTrend%2C" \
                    "upgradeDowngradeHistory%2C" \
                    "earnings%2C" \
                    "defaultKeyStatistics%2C" \
                    "balanceSheetHistory%2C" \
                    "assetProfile%2C" \
                    "cashflowStatementHistory%2C" \
                    "incomeStatementHistory%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
        summary_json_response = requests.get(query_url)

        final = {}

        json_loaded_summary = json.loads(summary_json_response.text)
        core = json_loaded_summary["quoteSummary"]["result"][0]
        processing_sets = [core[factor] for factor in core.keys()]

        if "calendarEvents" in core:
            if 'earnings' in core["calendarEvents"]:
                processing_sets.append(core["calendarEvents"]['earnings'])

        for ps in processing_sets:
            for x in list(ps.keys()):
                if isinstance(ps[x], dict):
                    if len(ps[x]) == 0:
                        ps[x] = None
                    elif 'raw' in ps[x]:
                        ps[x] = ps[x]['raw']

                if isinstance(ps[x], list):
                    ps[x] = [y['fmt'] for y in ps[x] if 'fmt' in y]

            final.update(ps)

        self.memoized_scraped_data[ticker] = (
            datetime.datetime.now(),
            final
        )

        self.info_keys[ticker] = final.keys()
        return final


    def __core_parse(self, ticker):
        if ticker in self.memoized_scraped_data:
            tuple = self.memoized_scraped_data[ticker]

            first_time = tuple[0]
            later_time = datetime.datetime.now()
            difference = later_time - first_time
            seconds_in_day = 24 * 60 * 60

            if divmod(difference.days * seconds_in_day + difference.seconds, 60)[0] < 15:
                thread = threading.Thread(target=self.____core_parse_helper, args=(ticker,))
                thread.start()

                return tuple[1]

        return self.____core_parse_helper(ticker)


    def get_available_data_tags(self, stock_ticker):
        if stock_ticker not in self.info_keys:
            self.get_company_data(stock_ticker)

        return self.info_keys[stock_ticker]

    def get_data_from_tag(self, stock_ticker, tag):
        if stock_ticker not in self.info_keys:
            self.get_company_data(stock_ticker)

        return self.memoized_scraped_data[stock_ticker][tag]


    def get_company_data(self, stock_ticker):
        core = self.__core_parse(stock_ticker)

        beta = core["beta"] if "beta" in core else None
        if beta is None:
            beta = core["beta3Year"] if "beta3Year" in core else None

        del core["beta3Year"]

        core["beta"] = beta

        return core


    def get_industry(self, stock_ticker):
        core = self.__core_parse(stock_ticker)
        return core["industry"]

    def get_sector(self, stock_ticker):
        core = self.__core_parse(stock_ticker)
        return core["sector"]

    def get_current_price(self, stock_ticker):
        core = self.__core_parse(stock_ticker)
        return core["currentPrice"]


    def get_ytd(self, stock_ticker):
        core = self.__core_parse(stock_ticker)
        return core['ytdReturn']


    def get_beta(self, stock_ticker):
        core = self.__core_parse(stock_ticker)

        beta = core["beta"] if "beta" in core else None
        if beta is None:
            beta = core["beta3Year"] if "beta3Year" in core else None

        return beta


    def get_purchase_recommendation(self, stock_ticker):
        core = self.__core_parse(stock_ticker)
        return core["recommendationMean"]

