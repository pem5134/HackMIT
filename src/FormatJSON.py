'''
@author: Peter Mason
         pm3.141@gmail.com
        
Created on Oct 5, 2014
'''

import json
import urllib.request

def getAllData(address):
    url = "https://bitcoin.toshi.io/api/v0/addresses/" + address + "/transactions"
    data = json.loads(urllib.request.urlopen(url).readall().decode("utf8"))
    return data


def getTransactions(address):
    allData = getAllData(address)
    transactions = allData['transactions']
    return transactions

def getChildren(address):
    children = []
    transactions = getTransactions(address)
    allOutput = transactions[0]['outputs']
    
    for transaction in transactions:
        children.append(transaction['outputs'][0]['addresses'][0])
    
    return children

global cache
global depth
depth = 0
cache = []


def createJSON(address):
    children = getChildren(address) #List of all immediate children
    numChildren = len(children)
    print('number of children: ', numChildren)
    root = {}
    root['name'] = address
    root['children'] = []
    
    if numChildren == 0:
        global depth
        depth = 0
        return root
    else:
        for child in children:
            print('child address: ', child)
            global depth
            global cache
            if(depth <= 3 and child not in cache):
                cache.append(child)
                print('in loop')
                depth += 1
                print(depth)
                root["children"].append(createJSON(child))   #createJSON(child)
    
    return root
    

address = "12f5KwWv4sMEcFjBLKsEuJhCXjv4crxmLL"


print(createJSON(address))
# print(getChildren(address))
