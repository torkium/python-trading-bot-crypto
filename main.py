from utils.View import View
from utils.Message import Message
from AppContext import AppContext
import traceback
from core.exchange.BinanceSpotExchange import BinanceSpotExchange
from core.Pair import Pair
from core.Wallet import Wallet
from strat.StratBtcSpot import StratBtcSpot as StratClass

try:
    AppContext.init()
    if AppContext.config["debug"]:
        View.print(Message.info("Debug Mode"))
    exchange = BinanceSpotExchange()
    wallet = Wallet(Pair("BTC", "USDT"), 100, 0)
    strat = StratClass(exchange=exchange, wallet=wallet)
    strat.run()
    View.print(Message.info("End"))
except Exception as err:
    print("Exception occured: {}".format(err))
    print(traceback.format_exc())
input("Push key to exit...")