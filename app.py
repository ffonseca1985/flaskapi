from flask import Flask, request
from db import items, stores
from flask_smorest import abort
import uuid

app = Flask(__name__)

@app.get("/store")
def get_store() -> dict[str, list[dict[{str, str}]]]:
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":  store_id}
    stores[store_id] = store
    return store, 201

@app.get("/store/<string:store_id>")
def get_store_by_id(store_id):
    try:
        return stores[store_id]
    except KeyError:
         abort(404, message="store not found")

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted"}
    except KeyError:
         abort(404, message="store not found")

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="store not found")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

@app.get("/item")
def get_all_items():
    return { "items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="item not found")

@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    try:
        item = items[item_id]
        item |= item_data #merge between dictionary

        return item
    except KeyError:
        abort(404, message="item not found" )


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message="item not found")
