
from main import app, cg
from flask import request, jsonify
import json
from forex_python.converter import CurrencyRates

class Coin():
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.ticker = data['ticker']
    self.current_price = data['current_price']
    self.market_cap = data['market_cap']
    self.vol24hr = data['vol24hr']
  
  def get_Coin_Dictionary(self):
    coin_Dict = {'id': self.id, 'name': self.name, 'ticker': self.ticker, 'price': self.current_price,'market_cap': self.market_cap,'vol24hr': self.vol24hr}
    return coin_Dict

    
class Portfolio_Coin(Coin):
  def __init__(self, data):
    super().__init__(data)
    self.purchase_Price = data['purchase_Price']
    self.purchase_DT = data['purchase_DT']
    self.purchase_QTY = data['purchase_QTY']

  """
  coin = {name: string, amount: number amount (0 if it has a future purchase date), date_purchased: datetime}
  """

  def get_Portfolio_Coin_Dictionary(self):
    coin_Portfolio_Dict = {'id': self.id, 'name': self.name, 'amount': self.purchase_QTY, 'date_purchased': self.purchase_DT}
    return coin_Portfolio_Dict


# def part_d(): Coin profitabiliy
#   d.) The tracker will create a custom profit/loss algorithm to evaluate real quantitative metrics surrounding a
#   Crypto. This profit/loss tracker will receive a Crypto name, the purchase amount. It will then calculate a profit/loss
#   based on the instantaneous value. (Bonus marks: if you can develop a robust algorithm to predict profit/loss based
#   on extrapolated “future” values of a specific crypto)
#    start date and end date
#   Solution:
#   Needs a portfoilio coin aka position and returns the profit in Percent and in USD
def coin_profitability(coin_id, amount, purchase_date, reference_date = None):
  if reference_date == None:
    current_price = getCrypto(coin_id, currency='usd')['price']
  else:
    current_price = prev_price(coin_id, reference_date)['price']
  
  purchase_price = prev_price(coin_id, purchase_date)['price']
  profit_usd = float(current_price)-float(purchase_price)
  profit_percent = profit_usd/purchase_price
  purchase_profit = amount * profit_usd
  return {'Profit %': profit_percent, 'Profit $': purchase_profit}


@app.route('/api/coins/search/<string:search_term>', methods=['GET'])
def search_coin(search_term):
  # Request coins based on the search tems
  coins = []
  coin_Gecko_List = cg.get_coins_list()

  for coin in coin_Gecko_List:
    if coin['name'].find(search_term) != -1:
      coin_current_price = cg.get_price(coin['id'], 'usd')[coin['id']]
      if bool(coin_current_price.values()) != -1:
        for value in coin_current_price.values():
          coin_current_price = value
          break
      else:
        coin_current_price = -1

      coin_dict = {'id': coin['id'], 'name': coin['name'], 'ticker':coin['symbol'], 'price': coin_current_price}
      coins.append(coin_dict)

  return json.dumps(coins)

  # """
  # {
  #   coins: [{
  #     id: string,
  #     name: string,
  #     ticker: string,
  #     current_price: number,
  #   }]
  # }
  # """
  # return ...

@app.route('/api/coin/<string:coin_id>/data', methods=['POST'])
def e(name):
  # Body will be is json format as:
  """
  {
    start_date: MM/DD/YYYY,
    end_date: MM/DD/YYYY
  }
  """
  body = request.body
  # Returns:
  """
  {
    data: number[], (size is numbers of days between start and end date)
    volatility: number, (variance)
  }
  """
  pass

@app.route('/api/coin/<string:coin_id>/date/<string:date>', methods=['GET'])
def prev_price(coin_id, date):
  # Return the price of the coin on a given date. The date of data snapshot in dd-mm-yyyy eg. 30-12-2017
  
  coinPriceDict = {"date": date}
  coinPriceDict['price'] = cg.get_coin_history_by_id(coin_id, date)['market_data']['current_price']['usd']

  return json.dumps(coinPriceDict)
  




# GET list of all availble coins
@app.route('/api/coins/list', methods=['GET'])
def coins_list():
  # Body will be is json format as:
  """
  {
    coin_id: string,
    name: string,
    symbol: string
  }
  """
  return json.dumps(cg.get_coins_list())

# GET price of crypto, coin ID, currency
@app.route('/api/coin/id/<string:id>/currency/<string:currency>', methods=['GET'])
def getCrypto(id, currency='usd'): 
  coinPriceDict = {}
  currencyDict = cg.get_price(ids = id, vs_currencies=currency)[id]

  if 'usd' in currencyDict.keys():
    coinPriceDict['price'] = currencyDict['usd']
  else:
    c = CurrencyRates()
    conversionRate = c.get_rate('USD', currency.upper())
    coinPriceDict['price'] = currencyDict[currency] / conversionRate

  return json.dumps(coinPriceDict)



