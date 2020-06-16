import threading
import requests
import json
import datetime


class TickerInfo:
    """
    TickerInfo can be used to get real-time financial information about assets listed in any global exchange. The module
    is powered with Yahoo Finance, and the tickers that can be used with TickerInfo are solely the ones permitted
    on Yahoo Finance.

    """
    def __init__(self):
        self.memoized_scraped_data = {}
        self.info_keys = {}

    def ____core_parse_helper(self, ticker):
        """ Scrapes Yahoo Finance to retrieve data about an asset ticker.

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (dict) Scraped data about asset ticker
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        query_url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US" \
                    "&region=US&modules=" \
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
        if json_loaded_summary is None \
                or "quoteSummary" not in json_loaded_summary\
                or "result" not in json_loaded_summary["quoteSummary"]\
                or len(json_loaded_summary["quoteSummary"]["result"]) == 0:
            return None

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
        """ Wrapper function on top of scraper function to assist with memoization process

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (dict) Scraped data about asset ticker
        """

        if ticker in self.memoized_scraped_data:
            data_tuple = self.memoized_scraped_data[ticker]

            first_time = data_tuple[0]
            later_time = datetime.datetime.now()
            difference = later_time - first_time
            seconds_in_day = 24 * 60 * 60

            if divmod(difference.days * seconds_in_day + difference.seconds, 60)[0] < 15:
                thread = threading.Thread(target=self.____core_parse_helper, args=(ticker,))
                thread.start()

                return data_tuple[1]

        return self.____core_parse_helper(ticker)

    def get_available_data_tags(self, ticker):
        """ Returns a list of available data for an asset ticker, as found in Yahoo Finance.

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (list) tags available for an asset ticker; Returns None if the information is not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        if ticker not in self.info_keys:
            self.get_company_data(ticker)

        return self.info_keys[ticker]

    def get_data_from_tag(self, ticker, tag):
        """ Returns available data for an asset ticker and a provided tag, as found in Yahoo Finance.

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :param tag: (String) Data tag that is to be retrieved from Yahoo Finance. For a list of
                    available data tags call TickerInfo.get_available_data_tags(tag)
        :return: (int or String) data associated with asset ticker and provided tag; Returns None if the information is
                 not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        if not isinstance(tag, str):
            raise TypeError("tag parameter is not a String")

        if ticker not in self.info_keys:
            self.get_company_data(ticker)

        return self.memoized_scraped_data[ticker][tag] if tag in self.memoized_scraped_data[ticker] else None

    def get_company_data(self, ticker):
        """ Returns a dictionary of data associated with the asset ticker, as found in Yahoo Finance. For a list of
            available data tags call TickerInfo.get_available_data_tags(tag).

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (dict) data associated with asset ticker; Returns None if the information is not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)

        if core is None or len(core) == 0:
            return None

        beta = core["beta"] if "beta" in core else None
        if beta is None:
            beta = core["beta3Year"] if "beta3Year" in core else None

        del core["beta3Year"]

        core["beta"] = beta

        return core if core is None else core

    def get_industry(self, ticker):
        """ Returns the industry of the company that is represented by the asset ticker. If the ticker is not of a stock
            the function will return None

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (String) the industry of the company represented by the asset ticker; Returns None if the information
                 is not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)
        return core if core is None else core["industry"]

    def get_sector(self, ticker):
        """ Returns the sector of the company that is represented by the asset ticker. If the ticker is not of a stock,
            the function will return None

        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (String) the sector of the company represented by the asset ticker; Returns None if the information is
                 not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)
        return core if core is None else core["sector"]

    def get_current_price(self, ticker):
        """ Returns the current price of the asset


        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (int) current price; Returns None if the information is not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)
        return core if core is None else core["currentPrice"]

    def get_ytd(self, ticker):
        """ Returns the year-to-date return of the requested asset


        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (int) year-to-date return; Returns None if the information is not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)
        return core if core is None else core['ytdReturn']

    def get_beta(self, ticker):
        """ Provides the beta coefficient for a given asset ticker. If the asset is a bond, the function returns the
            3-year beta coefficient


        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (int) beta coefficient; Returns None if the information is not available
        """

        core = self.__core_parse(ticker)

        beta = core["beta"] if "beta" in core else None
        if beta is None:
            beta = core["beta3Year"] if "beta3Year" in core else None

        return beta

    def get_purchase_recommendation(self, ticker):
        """ Provides analysts recommendation for purchasing a stock.
            1 – Strong Buy
            2 – Buy
            3 – Hold
            4 – Underperform
            5 – Sell


        :param ticker: (String) Asset ticker for globally listed companies, as supported by Yahoo Finance
        :return: (int) the number representation of stock purchase recommendation; Returns None if the information is
                 not available
        """

        if not isinstance(ticker, str):
            raise TypeError("ticker parameter is not a String")

        core = self.__core_parse(ticker)    
        return core if core is None else core["recommendationMean"]
