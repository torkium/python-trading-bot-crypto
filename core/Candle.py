import string, datetime
from decimal import Decimal

class Candle:
    __open_time:datetime
    __close_time:datetime
    __open:Decimal
    __close:Decimal
    __high:Decimal
    __low:Decimal
    __vol:Decimal

    def __init__(self, open_time:datetime, close_time:datetime, open:Decimal, close:Decimal, high:Decimal, low:Decimal, vol:Decimal) -> None:
        self.__open_time = open_time
        self.__close_time = close_time
        self.__open = open
        self.__close = close
        self.__high = high
        self.__low = low
        self.__vol = vol

    def getOpenTime(self) -> datetime:
        return self.__open_time

    def getCloseTime(self) -> datetime:
        return self.__close_time

    def getOpen(self) -> Decimal:
        return self.__open

    def getClose(self) -> Decimal:
        return self.__close

    def getHigh(self) -> Decimal:
        return self.__high

    def getLow(self) -> Decimal:
        return self.__low

    def getVol(self) -> Decimal:
        return self.__vol