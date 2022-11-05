from Pair import Pair
from decimal import Decimal
class Wallet:
    __pair:Pair
    __base_amount:Decimal
    __trade_amount:Decimal

    def __init__(self, pair:Pair, base_amount:Decimal, trade_amount=Decimal) -> None:
        self.__pair = pair
        self.__base_amount = base_amount
        self.__trade_amount = trade_amount

    def getPair(self) -> Pair:
        return self.__pair
    
    def getBaseAmount(self) -> Decimal:
        return self.__base_amount
    
    def getTradeAmount(self) -> Decimal:
        return self.__trade_amount