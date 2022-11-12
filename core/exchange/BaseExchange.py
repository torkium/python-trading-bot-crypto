import abc
from ..Candle import Candle

class BaseExchange(metaclass=abc.ABCMeta):
    
    async def waitNewCandle(self) -> Candle:
        pass