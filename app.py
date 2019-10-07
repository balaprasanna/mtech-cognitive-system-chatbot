from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

@app.route("/", methods=["GET" ,"POST"])
def main():
    req = request.get_json(silent=True, force=True)
    print(req)    
    coinname = req['queryResult']['parameters']['coinname']
    
    price = 7000 + random.randint(0,100)
    price = get_price(coinname)
    #weatherinfo = get_weather_info(location)
    resp = {
        "fulfillmentText": f" The price of {coinname} is {price}"
    }
    return jsonify(resp)

# UTIL FUNCTIONS....
def get_price(coinname):
  url = "https://api.coinmarketcap.com/v2/ticker/"
  resp  =requests.get(url)
  content = resp.json()
  price_dict = {}
  for key,value in content["data"].items():
    #print(value["name"],   value["quotes"]["USD"]["price"])
    k = value["name"].lower()
    v = value["quotes"]["USD"]["price"]
    price_dict[k] = v

  return price_dict.get(coinname, "Not found")

app.run(host='0.0.0.0', port=5000, debug=True)