
from flask.json import jsonify, request
from main import app
from coin import Coin

class WatchList():
  def __init__(self):
    self.coins = []

  def add_coin(self, coin):
    for existing_coin in self.coins:
      if existing_coin.id == coin.id:
        return 
    self.coins.append(coin)

  def remove_coin(self, coin):
    coin_to_remove = None
    for existing_coin in self.coins:
      if existing_coin.id == coin.id:
        coin_to_remove = existing_coin
    self.coins.remove(coin_to_remove)

  def get_json(self):
    coins = []
    for coin in self.coins:
      coins.append(coin.__repr__())
    return coins

watch_list = WatchList()

@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
  return jsonify(watch_list.get_json()), 200

@app.route('/api/watchlist/coin', methods=['POST', 'DELETE'])
def post_watchlist_coin():
  coin = request.json
  if request.method == 'GET':
    watch_list.add_coin(coin)
    return 200
  elif request.method == 'DELETE':
    watch_list.remove_coin(coin)
    return 200


