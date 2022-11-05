from Pair import Pair
import string
from BaseOrder import BaseOrder

class FuturePosition(BaseOrder):
    __pair:Pair
    __leverage:int
    __side:string

    # TODO: init function and getters