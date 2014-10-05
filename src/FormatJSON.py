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
        inputs = transaction["inputs"]
        outputs = transaction["outputs"]
        keep = False
        for inner in inputs:
            if inner["addresses"][0] == address:
                keep = True
        if keep:
            for output in outputs[0:5]:
                children.append(output["addresses"][0])
            # if(transaction['inputs'][0]['addresses'][0] == address):
            #     children.append(transaction['outputs'][0]['addresses'][0])
    
    #print("children: ", children)
    return children

def createJSON(address, depth):
    children = getChildren(address) #List of all immediate children
    transactions = getTransactions(address)
    size = 1000
    #print(children)

    if depth == 0:
        val = []
        print(len(children))
        for child in children[0:5]:
            for output in transactions[0]["outputs"]:
                if output["addresses"][0] == child:
                    print("got size", output["amount"])
                    size = 1000
            val.append({"name": child, "size": size})
        return val
    else:
        val = {}
        val["name"] = address
        
        if len(children) == 0:
            # for output in transactions[0]["outputs"]:
            #     if output["addresses"][0] == child:
            #         size = output["amount"]
            val["size"] = size
            return val
        else:
            val["children"] = []
            # for output in transactions[0]["outputs"]:
            #     if output["addresses"][0] == child:
            #         size = output["amount"]
            val["size"] = size
            for child in children[0:5]:
                if child != address:
                    if depth == 1:
                        print("Hey, Listen!", address, child)
                        if len(val["children"]) < 5:
                            val["children"] += createJSON(child, depth-1)
                    else:    
                        val["children"].append(createJSON(child, depth-1))
            #print(val)
            return val


    # print(children)
    # numChildren = len(children)
    # print('number of children: ', numChildren)
    # root = {}
    # root['name'] = address
    
    # if depth == 0:
    #     root['size'] = getTransactions(address)[0]["outputs"][0]["amount"]
    #     return root
    # else:
    #     root['children'] = []
    #     for child in children:
    #         print('child address: ', child)
    #         global cache
    #         if(depth <= 3 and child not in cache):
    #             cache.append(child)
    #             print('in loop')
    #             #depth += 1
    #             print(depth)
    #             root["children"].append(createJSON(child, depth-1))   #createJSON(child)
    
    # return root    

    # return {
    #     "name": "flare8000",
    #     "children": [
    #         {
    #         "name": "13D9F9zeBneXTjpbmcGdxGPcRmAs8UeokB", "size": 500
    #         },
    #         {"name": "test25", "size": 1000}
    #         ]
    #     }

address = "13D9F9zeBneXTjpbmcGdxGPcRmAs8UeokB"


#createJSON(address,2)
# print(getChildren(address))
