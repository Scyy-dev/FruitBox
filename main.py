from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

db = {
    "8ef25eca910c4dec86e10ba1ae1afdbd": 100000000000
}

@app.get("/fruitpoints/{player_uuid}")
async def get_player_points(
    player_uuid: Annotated[str, Path(pattern="^[0-9a-fA-F]{32}$")]
    ):
    if player_uuid in db:
        return {player_uuid: db[player_uuid]}
    return {"message": f"No items found for {player_uuid}"}
    
