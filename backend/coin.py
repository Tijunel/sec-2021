
from main import app, cg
from flask import request
import json

class Coin():
  def __init__(self, id, name, ticker, current_price, market_cap, vol24hr):
    self.id = id
    self.name = name
    self.ticker = ticker
    self.current_price = current_price
    self.market_cap = market_cap
    self.vol24hr = vol24hr

  def __init__(self, data):
    self.id = data.id
    self.name = data.name
    self.ticker = data.ticker
    self.current_price = data.current_price
    self.market_cap = data.market_cap
    self.vol24hr = data.vol24hr
  
  def __repr__(self):
    coin_Dict = {'id': self.id, 'name': self.name, 'ticker': self.ticker, 'current_price': self.current_price,'market_cap': self.market_cap,'vol24hr': self.vol24hr}
    return coin_Dict

    
class Portfolio_Coin(Coin):
  def __init__(self, purchase_price, purchase_DT, purchase_QTY):
    super().__init__()
    self.purchase_Price = purchase_price
    self.purchase_DT = purchase_DT
    self.purchase_QTY = purchase_QTY

  """
  coin = {name: string, amount: number amount (0 if it has a future purchase date), date_purchased: datetime}
  """
  def __repr__(self):
    coin_Portfolio_Dict = {'id': self.id, 'name': self.name, 'amount': self.purchase_QTY, 'date_purchased': self.purchase_DT}
    return coin_Portfolio_Dict


@app.route('/api/coins/<string:search_term>', methods=['GET'])
def d(search_term):
  # Request coins based on the search tems
  
  coins = []
  coin_Gecko_List = cg.get_coins_list()

  for coin in coin_Gecko_List:
    if coin.find("search_term"):
      coin_current_price = cg.get_coin_by_id(coin.id).price
      coin_dict = {'id': coin.id, 'name': coin.name, 'ticker':coin.symbol, 'price': coin_current_price}
      coins.append(coin)

  return coins


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

@app.route('/api/coin/<string:coin_id>/date/<string:date>')
def g(coin_id, date):
  # Return the price of the coin on a given date. 
  cg.get_coin_history_by_id(coin_id, date)
  pass

@app.route('/api/portfolio/<string:portfolio_id>/purchase', methods=['POST'])
def f(portfolio_id):
  # Body will be is json format as:
  """
  {
    coin_id: string,
    purchase_date: MM/DD/YYYY,
    amount: number
  }
  """
  body = request.body


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
def getCrypto(id=None, currency='usd'): 
  if id == None:
    return
  else:
    return json.dumps(cg.get_price(ids = id, vs_currencies=currency))
