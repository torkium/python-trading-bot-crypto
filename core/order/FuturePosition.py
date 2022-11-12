from Pair import Pair
import string
import string
import datetime
from decimal import Decimal
from .BaseOrder import BaseOrder

class FuturePosition(BaseOrder):
    __pair:Pair
    __leverage:int
    __side:string
    STATE_CLOSED:string = "closed"

    def __init__(self, id: string, pair:Pair, leverage:int, side:string, date: datetime, amount: Decimal, price: Decimal, state: string) -> None:
        super().__init__(id, date, amount, price, state)
        self.__pair = pair
        self.__leverage = leverage
        self.__side = side

    def getPair(self) -> Pair:
        return self.__pair

    def getLeverage(self) -> int:
        return self.__leverage

    def getSide(self) -> string:
        return self.__side