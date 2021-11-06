from main import app, cg
from flask import request, jsonify
import json
from datetime import *
from statistics import stdev

from coin import *
from watchlist import WatchList
from forex_python.converter import CurrencyRates

class Portfolio():
  def __init__(self):
    self.name = None
    self.id = None
    self.portfolio_coins = [] #list of coins in portfolio

  def addCoinToPortfolio(self, coin):
    self.portfolio_coins.append(coin)
  
  #Will return the detailed information of the portfolio in dict format
  def get_Portfolio_Coins(self):
    return self.portfolio_coins
    
#list of portfolios
portfolios = []

# FOR TESTING ONLY
test_portfolio = Portfolio()
test_portfolio.id = 0
test_portfolio.name = "My Test Portfolio"


testCoinData = {"id":"bitcoin", "name":"Bitcoin", "ticker":"BTC", "current_price":"76554", "market_cap": "104483022", "vol24hr": "4.32", "purchase_Price": "69.69", "purchase_DT": "11/01/2021", "purchase_QTY": "4"}
testCoinData1 = {"id":"eth5", "name":"Ethereum", "ticker":"ETH", "current_price":"5004", "market_cap": "45383902", "vol24hr": "2.45", "purchase_Price": "335.6", "purchase_DT": "11/01/2021", "purchase_QTY": "2"}
testCoinData2 = {"id":"dog4", "name":"Doge", "ticker":"DOG", "current_price":"1.22", "market_cap": "2384567", "vol24hr": "56.4", "purchase_Price": "33.45", "purchase_DT": "11/01/2021", "purchase_QTY": "1"}


a = Portfolio_Coin(testCoinData)
b = Portfolio_Coin(testCoinData1)
c = Portfolio_Coin(testCoinData2)

test_portfolio.addCoinToPortfolio(a)
test_portfolio.addCoinToPortfolio(b)
test_portfolio.addCoinToPortfolio(c)


portfolios.append(test_portfolio)


# def part_g():
#   for(portfolio in self.portfolio_list)
#   Using Daily RSI
# When the portfolio is passed through the evaluation tool the GUI must provide a conclusion:
# 1. Very High Risk
# 2. High Risk
# 3. Neutral
# 4. Low Risk
# 5. Very Low Risk
def risk_rating(portfolio):
  if(portfolio.portfolio_coins.length() == 0):
    return '400'
    
  # Find the earliest purchase in the portfolio
  min_date = portfolio.portfolio_coins[0].purchase_DT
  for coin in portfolio.portfolio_coins:
    if(coin.purchase_DT < min_date):
      min_date = coin.purchase_DT
  start_date = min_date  
  
  #End date is today
  end_date = datetime.today().strftime('%d-%m-%Y')
  
  portfolio_daily_value = []
  # Get the daily value of the portfolio since inception
  for single_date in daterange(start_date, end_date):
    coin_sum = 0
    for coin in portfolio.portfolio_coins:
      coin_sum += coin.purchase_QTY * prev_price(coin.id, single_date)['price']
    portfolio_daily_value.append(coin_sum)
  
  # Implement RSI with a 14 period moving average and levels of the following:
  # 1 > 75
  # 2 > 60
  # 3 45 < x < 60
  # 4 > 30
  # 5 < 15
  rsi_periods = 14
  gain = 0
  loss = 0
  for i in range(rsi_periods-1):
    difference = portfolio_daily_value.index(i+1) - portfolio_daily_value.index(i)
    if(difference > 0):
      gain+=append(difference)
    else:
      loss+=abs(difference)
  if (loss != 0):
    rs = gain/loss
  else:
    rs = gain/1      

  rsi = 100 - 100 / (1 + rs)
  print(rsi)

  if rsi > 75:
    risk_rating_portfolio = {'Rating': 1, 'Risk': "Very High Risk"}
  elif rsi > 60:
    risk_rating_portfolio = {'Rating': 2, 'Risk': "High Risk"}
  elif rsi > 45:
    risk_rating_portfolio = {'Rating': 3, 'Risk': "Neutral"}
  elif rsi > 30:
    risk_rating_portfolio = {'Rating': 4, 'Risk': "Low Risk"}
  else:
    risk_rating_portfolio = {'Rating': 5, 'Risk': "Very Low Risk"}

  return risk_rating_portfolio

# f.) Visualize total portfolio performance - Once again you should be able to visualize your total portfolio
# performance, while giving the user the ability to toggle which cryptos they want to visualize in their portfolio.
def visualize_total_portfolio(portfolio, start_date = None, date_end = None, filter_crypto = []):
  if(portfolio.portfolio_coins.length() == 0):
    return '400'
  if start_date == None:
    #Find the earliest purchase in the portfolio
    min_date = portfolio.portfolio_coins[0].purchase_DT
    for coin in portfolio.portfolio_coins:
      if(coin.purchase_DT < min_date):
        min_date = coin.purchase_DT
    start_date = min_date    
  if end_date == None:
    #End date is today
    compare_date_end = datetime.today().strftime('%d-%m-%Y')
  portfolio_daily_value = []
  
  if filter_crypto != []:
    portfolio_temp = []
    for coin in portfolio.portfolio_coins:
      for filter in filter_crypto:
        if filter != coin.name:
          portfolio_temp.append(coin)
  else:
    portfolio_temp = portfolio  
        
  for single_date in daterange(compare_date_start, compare_date_end):
    coin_sum = 0
    for coin in portfolio_temp.portfolio_coins:
      coin_sum += coin.purchase_QTY * prev_price(coin.id, single_date)['price']
    portfolio_daily_value.append({"Day": single_date, "Price": coin_sum})
  return json.dump(portfolio_daily_value)

# e.) Compare asset performance - For each asset, the tracker should be able to compare the performance of each
# asset from their buy date to the present, with the performance of major crypto such as Bitcoin and Ethereum
# during that date range. This comparison should be visualized as well

# Solution:
# Will recieve the information of two Portfolio coins and call the coin_profitability from coin to compare
def compare_two_coins_percent(coin_id_one, coin_id_two, compare_date_start, amount=0, compare_date_end = None):
  if compare_date_end == none:
    coin_one_profitability = coin_profitability(coin_id_one,amount,compare_date_start)
    coin_two_profitability = coin_profitability(coin_id_two,amount,compare_date_start)
  else:
    coin_one_profitability = coin_profitability(coin_id_one,amount,compare_date_start,compare_date_end)
    coin_two_profitability = coin_profitability(coin_id_two,amount,compare_date_start,compare_date_end)
  return {'Profit % Coin 1': coin_one_profitability, 'Profit % Coin 2': coin_two_profitability}

def compare_two_coins_daily_prices(coin_id_one, coin_id_two, compare_date_start, compare_date_end = None):
  coin_one_daily_prices = []
  coin_two_daily_prices = []
  if compare_date_end == None:
    compare_date_end = datetime.today().strftime('%d-%m-%Y')
  for single_date in daterange(compare_date_start, compare_date_end):
    print(single_date.strftime("%d-%m-%Y"))
    coin_one_daily_prices.append({"Day": single_date, "Price": prev_price(coin_id_one, single_date)['price']})
    coin_two_daily_prices.append({"Day": single_date, "Price": prev_price(coin_id_two, single_date)['price']})

  return json.dump([coin_one_daily_prices,coin_two_daily_prices])

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# WORKING
@app.route('/api/portfolios', methods=['GET'])
def get_():
  # Return the high-level data of each portfolio in the format:
  """
  [{
    portfolio_id: number,
    name: string,
  }]
  """
  result = []
  for portfolio in portfolios:
    result.append({"portfolio_id":portfolio.id, "name":portfolio.name})

  return json.dumps(result)

# POST create portfolio, accepts portfolio title
@app.route('/api/portfolio/<string:portfolio_name>', methods = ['POST'])
def create_portfolio(portfolio_name):
  # create a new portfolio with specified name
  # no error checking so can have two portoflios with same name
  new_portfolio = Portfolio()
  new_portfolio.name = portfolio_name
  new_portfolio.id = max(portfolio.id for portfolio in portfolios) + 1
  portfolios.append(new_portfolio)
  print(portfolios)

  return json.dumps({
    "portfolio_id": new_portfolio.id,
    "name": new_portfolio.name
  }), 200


@app.route('/api/portfolio/<int:portfolio_id>', methods=['GET'])
def a(portfolio_id):
  # Return the portfolio's detailed information
  """
  {
    coins: [{
      id: string,
      name: string,
      amount : number, (0 if it has a future purchase data),
      date_purchased: datetime, (could be in the future)
    }],
  }
  """
  #Will need to make sure that the portfolio list is properly formatted
  for portfolio in portfolios:
    if portfolio.id == portfolio_id:
      coinList = portfolio.get_Portfolio_Coins()
      jsonCoinList = []
      for coin in coinList:
        jsonCoinList.append(json.dumps(coin.get_Coin_Dictionary()))
      return json.dumps(jsonCoinList)


@app.route('/api/portfolio/<int:portfolio_id>/returns', methods=['POST'])
def c(portfolio_id):
  # Body will be is json format as:
  """
  {
    start_date: MM/DD/YYYY,
    end_date: MM/DD/YYYY
  }
  """
  
  # Returns:
  """
  {
    price_data: number[], (size is numbers of days between start and end date)
    volatility: number, (variance)
    percent_data: number[]: %total return daily
  }
  """
  body = request.json
  date_start = datetime.strptime(body['start_date'], '%d-%m-%Y')
  date_end = datetime.strptime(body['end_date'], '%d-%m-%Y')
  
  daily_data = []
  percent_data = []
  
  # find the requested portfolio ID
  for portfolio in portfolios:
    if portfolio.id == portfolio_id:
      if(len(portfolio.portfolio_coins) ==0):
        return '400'
      # start with first day for each coin in list
      # int(date_end-date_start).days)
      for single_date in (date_start + timedelta(n) for n in range(5)):
        coin_sum = 0
        for coin in portfolio.portfolio_coins:
          # if coin is being filtered ignore
          # add up value of coin on given day and add to total
          print(coin)
          coin_sum += coin.purchase_QTY * prev_price(coin.id, single_date)['price']
        daily_data.append(coin_sum)

      # calculate return from start date
      for price in daily_data:
        per_return = (price - daily_data[0]) / daily_data[0]
        percent_data.append(per_return)
        
      volatility = statistics.stdev(percent_data)
      
  return {"price_data": daily_data, "percent_data": percent_data, "volatility": volatility}    

  
  
  # start with day 1, add up the prices for each portcolio coin on that day
  # do this for every day in date range requested
  # after we have range
  
  
  # If type is "returns", data should be in percentage,
  # If type is "dollars", data should be in USD
  
  # per day price and single percent return of total portfolio
  


# # POST buy crypto, accepts date, purchase amount, market order price
# @app.route('/api/portfolio/positions/addposition ', methods=['POST'])

# # POST buy crypto, purchase amount, market order price
@app.route('/api/portfolio/<int:portfolio_id>/purchase', methods=['POST'])
def purchase_Crypto(portfolioID):
  body = request.json

  print(body)
  cryptoInfo = cg.get_coin_by_id(body['coin_id'])

  currencyDict = cg.get_price(ids = id, vs_currencies='usd')[id]
  coinPrice = currencyDict['usd']

  # today = date.today()
  # purchaseDate = today.strftime("%b-%d-%Y")
  added_coin = Portfolio_Coin(body['coin_id'], cryptoInfo['name'], cryptoInfo['ticker'], coinPrice, cryptoInfo['market'], cryptoInfo['vol24hr'], coinPrice, body['purchaseDate'], body['amount'])
  portfolios[portfolioID].addCoinToPortfolio(added_coin)
  return '200'


# @app.route('/api/portfolio/<string:portfolio_id>/purchase', methods=['POST'])
# def f(portfolio_id):
#   # Body will be is json format as:
#   """
#   {
#     coin_id: string,
#     purchase_date: MM/DD/YYYY,
#     amount: number
#   }
#   """
#   body = request.body
#   pass