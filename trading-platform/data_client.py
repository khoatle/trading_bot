import abc
# Separate quandl into another file
import quandlXZ
import re


class TradeClientFactory(abc.ABC):
    def create_client(self):
        pass


class QuandlClientFactory(TradeClientFactory):
    api_key = ''
    api_version = ''

    def __init__(self, api_config_provider):
        self.api_version = api_config_provider.api_version
        self.api_key = api_config_provider.api_key


    def create_client(self):
        return QuandlServiceClient(self.api_key, self.api_version)


class ExchangeServiceClient(abc.ABC):
    def get_trades(self, symbol, start_date, end_date):
        pass

    def list_symbols(self, start_date, end_date):
        pass


class QuandlServiceClient(ExchangeServiceClient):
    default_database = 'WIKI'

    def __init__(self, api_key, api_version):
        quandl.ApiConfig.api_key = api_key
        quandl.ApiConfig.api_version = api_version

    def get_trades(self, symbol, start_date, end_date):
        # Where a ticker contains a . or -, this is removed from the ticker we use. For example,
        # BRK.B is BRKB
        symbol = re.sub(r"[-,]", '', symbol)

        database_symbol = "({database}/{symbol})".format(database=self.default_database, symbol=symbol)
        return quandl.Dataset(database_symbol).data(params={
            'start_date': start_date,
            'end_date': end_date
        })

    def list_symbols(self, start_date, end_date):
        pass

