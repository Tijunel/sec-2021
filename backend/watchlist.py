
from flask.json import jsonify, request
from main import app
from coin import Coin

class WatchList():
  def __init__(self):
    self.coins = []

  def add_coin(self, coin):
    for existing_coin in self.coins:
        if existing_coin.get_Coin_Dictionary()['id'] == coin['id']:
          return 
    self.coins.append(Coin(coin))

  def remove_coin(self, coin):
    index_to_remove = -1
    for i, existing_coin in enumerate(self.coins):
      print(coin, existing_coin)
      if existing_coin.__repr__()['id'] == coin['id']:
        index_to_remove = i
    self.coins.pop(index_to_remove)

  def get_json(self):
    coins = []
    for coin in self.coins:
      coins.append(coin.get_Coin_Dictionary())
    return coins

watch_list = WatchList()

testCoinData = {"id":"bitcoin", "name":"bitcoin", "ticker":"btc", "current_price":76000, "market_cap": 0, "vol24hr": 0}
watch_list.add_coin(Coin(testCoinData))

@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
  return jsonify(watch_list.get_json()), 200

@app.route('/api/watchlist/coin', methods=['POST', 'DELETE'])
def post_watchlist_coin():
  coin_to_update = request.json
  if request.method == 'POST':
    print(coin_to_update['id'])
    watch_list.add_coin(coin_to_update)
    return '200'
  elif request.method == 'DELETE':
    watch_list.remove_coin(coin_to_update)
    return '200'


