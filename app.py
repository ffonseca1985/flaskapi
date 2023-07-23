from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "myStore",
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
