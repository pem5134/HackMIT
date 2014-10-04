
#import json

#import urllib2

from flask import Flask, render_template

#json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

#url = "https://bitcoin.toshi.io/api/v0/addresses/13D9F9zeBneXTjpbmcGdxGPcRmAs8UeokB/transactions"

#data = json.load(urllib2.urlopen(url))

#dest = data["transactions"][0]["outputs"]

#for i in range(len(dest)):
#	print dest[i]["addresses"], input[i]["amount"] / 100000000.0

#print input

# prev = data["inputs"][0]["previous_transaction_hash"]

# url2 = "https://bitcoin.toshi.io/api/v0/transactions/" + prev

# data2 = json.load(urllib2.urlopen(url))

# print data2["outputs"][0]["addresses"]


# def getTransactions(address):
# 	url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
# 	data = json.load(urllib2.urlopen(url))
# 	dests = data["transactions"][0]["outputs"]
# 	children = []
# 	for dest in dests:
# 		children.append((dest["addresses"][0], dest["amount"]))
# 	return children

import json
import urllib.request
import sys

def getTransactions(address):
	url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
	data = json.loads(urllib.request.urlopen(url).readall().decode("utf8"))
	dests = data["transactions"][0]["outputs"]
	children = []
	for dest in dests:
		children.append((dest["addresses"][0], dest["amount"]))
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