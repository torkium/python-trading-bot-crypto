import string

class Pair:
    __base_currency:string
    __trade_currency:string

    def __init__(self, base_currency:string, trade_currency:string) -> None:
        self.__base_currency = base_currency
        self.__trade_currency = trade_currency

    def getBaseCurrency(self) -> string:
        return self.__base_currency

    def getTradeCurrency(self) -> string:
        return self.__trade_currency