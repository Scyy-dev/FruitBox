from fastapi import FastAPI

app = FastAPI()

db = {
    "apples": 5,
    "oranges": 3
}

@app.get("/{item_id}")
async def root(item_id: str):
    if item_id in db:
        return {item_id: db[item_id]}
    return {"message": f"No items found for {item_id}"}
