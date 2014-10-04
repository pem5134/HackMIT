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

print(children)
	
# url = "https://bitcoin.toshi.io/api/v0/addresses/12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX/transactions"

# response = urllib.request.urlopen(url)

# str = response.readall().decode("utf-8")

# data = json.loads(str)

# print(data)
