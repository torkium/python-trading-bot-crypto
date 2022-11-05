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

    # TODO: init function and getters