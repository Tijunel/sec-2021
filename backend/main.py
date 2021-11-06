
from flask import (Flask, send_from_directory)

from pycoingecko import CoinGeckoAPI
# coinGECKOAPIBase = https://api.coingecko.com/api/v3
cg = CoinGeckoAPI()
app = Flask(__name__, static_folder='../client/build')
from portfolio import *
from watchlist import *
from coin import *

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve_react_app(path):
#   if path != "" and os.path.exists(app.static_folder + '/' + path):
#     return send_from_directory(app.static_folder, path)
#   else:
#     return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
  app.run(port=4000, host="0.0.0.0", debug=True)