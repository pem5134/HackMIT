
# get child addresses from each transaction at a given address

from flask import Flask, render_template

import json
import urllib.request
import sys

def getTransactions(address):
	url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
	data = json.loads(urllib.request.urlopen(url).readall().decode("utf8"))
	children = []
	for transaction in data["transactions"]:
		dests = transaction["outputs"]
		current = []
		for dest in dests:
			current.append((dest["addresses"][0], dest["amount"]))
		children.extend([current])
	return children

address = "1AeZL1f5YSDo6bhMcinuU3xFZgVjffYyPQ"

children = getTransactions(address)

app = Flask(__name__)
app.debug = False

@app.route("/")
def home():
  children = getTransactions("13D9F9zeBneXTjpbmcGdxGPcRmAs8UeokB")
  return render_template("index.html", children = children)

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
  app.run()