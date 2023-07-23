from flask import Flask

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