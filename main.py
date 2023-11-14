from fastapi import FastAPI

app = FastAPI()

db = {
    "player1": 5,
    "player2": 3,
    "scyphers": 100000000000
}

@app.get("/fruitpoints/{player_uuid}")
async def get_player_points(player_uuid: str):
    if player_uuid in db:
        return {player_uuid: db[player_uuid]}
    return {"message": f"No items found for {player_uuid}"}
    
