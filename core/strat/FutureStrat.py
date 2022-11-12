from typing import List
from .BaseStrat import BaseStrat
from ..indicator.BaseIndicator import BaseIndicator
from ..exchange.BaseExchange import BaseExchange
from ..Wallet import Wallet
from ..order.FuturePosition import FuturePosition

class FutureStrat(BaseStrat):
    __positions:List[FuturePosition]

    def __init__(self, exchange: BaseExchange, wallet: Wallet, positions:List[FuturePosition] = []) -> None:
        super().__init__(exchange, wallet)
        self.__positions = positions

    def getPositions(self) -> List[FuturePosition]:
        return self.__positions

    def hasOpenedPosition(self) -> bool:
        return False