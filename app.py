from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "itens": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_store() -> dict[str, list[dict[{str, str}]]]:
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)

    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name: str):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            newitem = {"name": request_data["name"], "price": request_data["price"]}
            store["itens"].append(newitem)
            return newitem, 201
    return {"message": "store not found"}, 404