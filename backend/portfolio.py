from main import app, cg
from flask import request, jsonify
import json

from coin import Coin, Portfolio_Coin
from watchlist import WatchList

class Portfolio():
  def __init__(self):
    self.name = None
    self.id = None
    self.portfolioList = [] #list of coins in portfolio

  
  def addCoinToPortfolio(self, coin):
    self.portfolio.append(coin)

#Will return the detailed information of the portfolio in dict format
  def __repr__(self):
    return self.portfolioList
    
#list of portfolios
portfolios = []

# FOR TESTING ONLY
test_portfolio = Portfolio()
test_portfolio.id = 0
test_portfolio.name = "My Test Portfolio"
portfolios.append(test_portfolio)

# POST create portfolio, accepts portfolio title

@app.route('api/portfolio/<string:portflio_name>', method = ['GET'])
def get_():
  # create a new portfolio with specified name
  args = request.args
  
  new_portfolio = Portfolio()
  new_portfolio.name = args["portfolio_name"]
  new_portfolio.id = max(portfolio.id for portfolio in portfolios) + 1

  return '1'

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
    result.append({portfolio.id:portfolio.name})

  return json.dumps(result)

@app.route('/api/portfolio/<int:portfolio_id>', methods=['GET'])
def a(portfolio_id):
  # Return the portfolio's detailed information

  #Will need to make sure that the portfolio list is properly formatted
  for portfolio in portfolios:
    if portfolio.id == portfolio_id:
      return json.dumps(portfolios[portfolio_id])

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

@app.route('/api/portfolio/<int:portfolio_id>/profits/<string:type>', methods=['POST'])
def c(portfolio_id, type):
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
  # If type is "returns", data should be in percentage,
  # If type is "dollars", data should be in USD
  pass

# # POST buy crypto, accepts date, purchase amount, market order price
# @app.route('/api/portfolio/positions/addposition ', methods=['POST'])

# pass
# # POST buy crypto, purchase amount, market order price
# @app.route('/api/portfolio/positions/addpositionnow ', methods=['POST'])
  
# pass