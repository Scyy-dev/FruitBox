from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

# === Regex Patterns === 
PLAYER_UUID_REGEX = "^[a-f0-9]{32}$"
TEAM_ID_REGEX = "^[a-zA-Z]\w{4,31}$"
TEAM_PREFIX_REGEX = "^[a-zA-Z]\w{1,5}$"

# Random UUIDs for testing
db = {
    "team1": {
        "prefix": "[team1] ",
        "players": {
            "dbfa1ca13bb64adc9a89dc6e4bd86895": 5,
            "c1152ca0b5f245639224299cf28cf107": 10,
            "53c03449389f4f1ca2b08371354adf56": 15
        }
    },
    "team2": {
        "prefix": "[t2] ",
        "players": {
            "dcedddeedc7e46d2be536b21221b59e0": 0,
            "0c4f481413a14f528d3e71e1bf90495e": 20,
            "bfd662842c124f16813618f7d17ed36d": 8
        }
    }
}

NOT_IMPLEMENTED = {"Error": "Not implemented yet"}

# === Team-Specific Operations

@app.get("/fruit_teams/teams/{team_id}/points")
async def get_team_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.get("/fruit_teams/teams/{team_id}/members")
async def get_team_members(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.get("/fruit_teams/teams/{team_id}/prefix")
async def get_team_prefix(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.put("/fruit_teams/teams/{team_id}/{player_uuid}")
async def add_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.delete("/fruit_teams/teams/{team_id}/{player_uuid}")
async def remove_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.get("/fruit_teams/teams/{team_id}/{player_uuid}")
async def get_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.patch("/fruit_teams/teams/{team_id}/{player_uuid}/{points}")
async def set_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)],
    points: Annotated[int, Path(gt=0)]
):
    return NOT_IMPLEMENTED
    

# === Team Management ===

@app.post("/fruit_teams/teams/{team_id}")
async def create_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    prefix: Annotated[str, Query(pattern=TEAM_PREFIX_REGEX)]
):
    return NOT_IMPLEMENTED

@app.get("/fruit_teams/random_team/{player_uuid}")
async def add_to_random_team(
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@app.delete("/fruit_teams/teams/{team_id}")
async def delete_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

# === Leaderboards ===

@app.get("/fruit_teams/leaderboard/top_10_teams")
async def get_top_10_teams():
    return NOT_IMPLEMENTED

@app.get("/fruit_teams/leaderboard/top_10_players")
async def get_top_10_players():
    return NOT_IMPLEMENTED
