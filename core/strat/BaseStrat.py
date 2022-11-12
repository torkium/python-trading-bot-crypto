from typing import List
from ..Wallet import Wallet
from ..exchange.BaseExchange import BaseExchange
from ..indicator.BaseIndicator import BaseIndicator
import abc

class BaseStrat(metaclass=abc.ABCMeta):
    __indicators:List[BaseIndicator]
    __exchange:BaseExchange
    __wallet:Wallet

    def __init__(self, exchange:BaseExchange, wallet:Wallet) -> None:
        self.__exchange = exchange
        self.__wallet = wallet

    def getIndicators(self) -> List[BaseIndicator]:
        return self.__indicators

    def getExchange(self) -> BaseExchange:
        return self.__exchange

    def getWallet(self) -> Wallet:
        return self.__wallet

    def addIndicator(self, indicator:BaseIndicator) -> None:
        self.__indicators.append(indicator)

    def run(self) -> None:
        pass