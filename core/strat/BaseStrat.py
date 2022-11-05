from typing import List
from ..Wallet import Wallet
from ..exchange.BaseExchange import BaseExchange
from ..indicator.BaseIndicator import BaseIndicator
import abc

class BaseStrat(metaclass=abc.ABCMeta):
    __indicators:List[BaseIndicator] = []
    __exchange:BaseExchange = None
    __wallet:Wallet = None

    def __init__(self, indicators:List[BaseIndicator], exchange:BaseExchange, wallet:Wallet) -> None:
        self.__indicators = indicators
        self.__exchange = exchange
        self.__wallet = wallet

    def getIndicators(self) -> List[BaseIndicator]:
        return self.__indicators

    def getExchange(self) -> BaseExchange:
        return self.__exchange

    def getWallet(self) -> Wallet:
        return self.__wallet