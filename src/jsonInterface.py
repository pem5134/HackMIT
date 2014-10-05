
# get child addresses from each transaction at a given address

from flask import Flask, render_template, jsonify, request

import json
import urllib.request
import sys

def getTransactions(address):
	url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
	data = json.loads(urllib.request.urlopen(url).readall().decode("utf8"))
	return data
	# children = []
	# for transaction in data["transactions"]:
	# 	dests = transaction["outputs"]
	# 	current = []
	# 	for dest in dests:
	# 		current.append((dest["addresses"][0], dest["amount"]))
	# 	children.extend([current])
	# return children

address = "1AeZL1f5YSDo6bhMcinuU3xFZgVjffYyPQ"

app = Flask(__name__)
app.debug = False

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/data")
def data():
	children = getTransactions("13D9F9zeBneXTjpbmcGdxGPcRmAs8UeokB")
	return json.dumps(children)

@app.route('/_array2python')
def sendToPython():
	wordList = request.args.get('wordlist')
	return jsonify(result=wordList)

@app.route('/tree.html')
def tree():
	return render_template("tree.html")

@app.route('/flare.json')
def flare():
	with open("templates/flare.json", "r") as myfile:
		data=myfile.read().replace('\n', '')
	return data

@app.route('/_getData')
def getData():
	address = request.args.get('word', type=str)
	children = getTransactions(address)
	tree = createJson(children["transactions"], address, 2)	
	with open("templates/current.json", "w") as outfile:
		json.dump(tree, outfile)
	return jsonify(result=tree)

def createJson(transactions, address, depth):
	print("depth:", depth)
	if depth == 1:
		leaves = []
		for transaction in transactions:
			inputs = transaction["inputs"]
			outputs = transaction["outputs"]
			keep = False
			for inner in inputs:
				if inner["addresses"][0] == address:
					keep = True
			if keep:
				for output in outputs:
					leaves.append({"name": transaction["outputs"][0]["addresses"][0],
						   "size": transaction["outputs"][0]["amount"]})
		if leaves != []:
			return leaves[0]
		return leaves
	else:
		tree = {}
		tree["name"] = address
		tree["children"] = []
		print(tree)
		for child in transactions:
			print(1)
			#print("child:", child)
			inputs = child["inputs"]
			outputs = child["outputs"]
			keep = False
			print(2)
			for inner in inputs:
				if inner["addresses"][0] == address:
					print("got one")
					keep = True
			if keep:
				for output in outputs:
					print("we did it!")
					print(output)
					newAddress = output["addresses"][0]
					newData = getTransactions(newAddress)
					print("or did we?")
					tree["children"].append(createJson(newData["transactions"],
											newAddress, depth-1))
					
	return tree


if __name__ == "__main__":
  app.run()

