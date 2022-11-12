import abc
import string
import datetime
from decimal import Decimal

class BaseOrder(metaclass=abc.ABCMeta):
    __id:string
    __date:datetime
    __amount:Decimal
    __price:Decimal
    __state:string
    STATE_OPEN:string = "open"
    STATE_FILLED:string = "filled"

    def __init__(self, id:string, date:datetime, amount:Decimal, price:Decimal, state:string) -> None:
        self.__id = id
        self.__date = date
        self.__amount = amount
        self.__price = price
        self.__state = state

    def getId(self) -> string:
        return self.__id

    def getDate(self) -> datetime:
        return self.__date

    def getAmount(self) -> Decimal:
        return self.__amount

    def getPrice(self) -> Decimal:
        return self.__price

    def getState(self) -> string:
        return self.__state