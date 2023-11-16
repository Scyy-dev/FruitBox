from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

# === Regex Patterns === 
PLAYER_UUID_REGEX = "^[a-f0-9]{32}$"
TEAM_ID_REGEX = "^[a-zA-Z]\\w{4,31}$"
TEAM_PREFIX_REGEX = "^[a-zA-Z]\\w{1,5}$"

# === Errors ===
NOT_IMPLEMENTED = HTTPException(status_code=500, detail="Endpoint not implemented")
PLAYER_ALREADY_EXISTS = HTTPException(status_code=404, detail="Player already exists")

# === Other Stuff ===

# Random UUIDs for testing
db = {
    "team1": {
        "prefix": "[team1] ",
        "members": {
            "dbfa1ca13bb64adc9a89dc6e4bd86895": 5,
            "c1152ca0b5f245639224299cf28cf107": 10,
            "53c03449389f4f1ca2b08371354adf56": 15
        }
    },
    "team2": {
        "prefix": "[t2] ",
        "members": {
            "dcedddeedc7e46d2be536b21221b59e0": 0,
            "0c4f481413a14f528d3e71e1bf90495e": 20,
            "bfd662842c124f16813618f7d17ed36d": 8
        }
    }
}

# === Team-Specific Operations

@app.get("/fruitteams/teams/{team_id}/points", tags=["FruitTeams", "Team-Specific Operations"])
async def get_team_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    point_total = 0
    team_members = db[team_id]["members"]
    for member in team_members:
        point_total += team_members[member]

    return { "points": point_total }

@app.get("/fruitteams/teams/{team_id}/members", tags=["FruitTeams"])
async def get_team_members(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    team_members: dict = db[team_id]["members"]
    return { "members": team_members.keys }

@app.get("/fruitteams/teams/{team_id}/prefix", tags=["FruitTeams"])
async def get_team_prefix(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    prefix = db[team_id]["prefix"]
    return { "prefix": prefix }

@app.put("/fruitteams/teams/{team_id}/{player_uuid}", tags=["FruitTeams"])
async def add_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    team_members: dict = db[team_id]["members"]
    if player_uuid in team_members:
        raise PLAYER_ALREADY_EXISTS
    return {"Result": "Success"}

@app.delete("/fruitteams/teams/{team_id}/{player_uuid}", tags=["FruitTeams"])
async def remove_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    raise NOT_IMPLEMENTED

@app.get("/fruitteams/teams/{team_id}/{player_uuid}", tags=["FruitTeams"])
async def get_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.patch("/fruitteams/teams/{team_id}/{player_uuid}/{points}", tags=["FruitTeams"])
async def set_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)],
    points: Annotated[int, Path(gt=0)]
):
    return NOT_IMPLEMENTED
    

# === Team Management ===

@app.post("/fruitteams/teams/{team_id}", tags=["FruitTeams"])
async def create_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    prefix: Annotated[str, Query(pattern=TEAM_PREFIX_REGEX)]
):
    return NOT_IMPLEMENTED

@app.get("/fruitteams/random_team/{player_uuid}", tags=["FruitTeams"])
async def add_to_random_team(
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.delete("/fruitteams/teams/{team_id}", tags=["FruitTeams"])
async def delete_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

# === Leaderboards ===

@app.get("/fruitteams/leaderboard/top_10_teams", tags=["FruitTeams"])
async def get_top_10_teams():
    return NOT_IMPLEMENTED

@app.get("/fruitteams/leaderboard/top_10_players", tags=["FruitTeams"])
async def get_top_10_players():
    return NOT_IMPLEMENTED
