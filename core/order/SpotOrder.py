import string
import string
import datetime
from decimal import Decimal
from .BaseOrder import BaseOrder

class SpotOrder(BaseOrder):
    __currency:string

    def __init__(self, id: string, currency:string, date: datetime, amount: Decimal, price: Decimal, state: string) -> None:
        super().__init__(id, date, amount, price, state)
        self.__currency = currency
    
    def getCurrency(self) -> string:
        return self.__currency