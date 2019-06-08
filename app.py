from flask import Flask, jsonify , request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'my store',
        'items': [
            {
                'name':'my item',
                'price':5
            }
        ]
    }
]

@app.route("/")
def index():
    return render_template("index.html")

# post
@app.route("/store",methods=['POST'])
def addStore():
    # retrieve data in flask(converts json to python dict)
    request_data = request.get_json()
    new_store = {
            'name':request_data['name'],
            'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# get storeName note: Browser undertstands get method by default
@app.route("/store/<string:name>")
def getStoreName(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})

# get All stores endpoint
@app.route("/store")
def getAllStore():
# {"stores":stores} because stores is a python dict, using directly will throw error
    return jsonify({'stores':stores})

# post item name and price for store endpoint
@app.route("/store/<string:name>/item",methods=["POST"])
def addNamePrice(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {
                    'name':request_data['name'],
                    'price':request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

# get store items endpoint
@app.route("/store/<string:name>/item")
def getItemsInStore(name):
    for store in  stores:
        if store['name'] == name:
            return jsonify({"items":store['items']})
    return jsonify({'message':'store not found'})



if __name__ == "__main__":
    app.run(port=3000,debug=True,threaded=True)
