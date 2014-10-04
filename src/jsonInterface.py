
import json

import urllib2

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


def getTransactions(address):
	url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
	data = json.load(urllib2.urlopen(url))
	dests = data["transactions"][0]["outputs"]
	children = []
	for dest in dests:
		children.append((dest["addresses"][0], dest["amount"]))
	return children
