from typing import List
from .BaseStrat import BaseStrat
from ..indicator.BaseIndicator import BaseIndicator
from ..exchange.BaseExchange import BaseExchange
from ..Wallet import Wallet
from ..order.SpotOrder import SpotOrder

class SpotStrat(BaseStrat):
    __orders:List[SpotOrder]

    def __init__(self, indicators: List[BaseIndicator], exchange: BaseExchange, wallet: Wallet, orders:List[SpotOrder]) -> None:
        super().__init__(indicators, exchange, wallet)
        self.__orders = orders

    def getOrders(self) -> List[SpotOrder]:
        return self.__orders