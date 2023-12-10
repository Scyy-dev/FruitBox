from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query

# === Regex Patterns === 
PLAYER_UUID_REGEX = r"[a-f0-9]{32}"
TEAM_ID_REGEX = r"^[a-zA-Z]\w{4,31}$"
TEAM_PREFIX_REGEX = r"^[a-zA-Z]\w{1,5}$"

# === Errors ===
NOT_IMPLEMENTED = HTTPException(status_code=500, detail="Endpoint not implemented")
PLAYER_ALREADY_EXISTS = HTTPException(status_code=404, detail="Player already exists")

# === FastAPI Router ===
router = APIRouter(
    prefix="/fruit_teams",
    tags=["fruit_teams"]
)

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

@router.get("/fruit_teams/teams/{team_id}/points")
async def get_team_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    point_total = 0
    team_members = db[team_id]["members"]
    for member in team_members:
        point_total += team_members[member]

    return { "points": point_total }

@router.get("/fruit_teams/teams/{team_id}/members")
async def get_team_members(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    team_members: dict = db[team_id]["members"]
    
    return { "members": list(team_members.keys()) }

@router.get("/fruit_teams/teams/{team_id}/prefix")
async def get_team_prefix(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    prefix = db[team_id]["prefix"]
    return { "prefix": prefix }

@router.put("/fruit_teams/teams/{team_id}/{player_uuid}")
async def add_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    team_members: dict = db[team_id]["members"]
    if player_uuid in team_members:
        raise PLAYER_ALREADY_EXISTS
    return {"Result": "Success"}

@router.delete("/fruit_teams/teams/{team_id}/{player_uuid}")
async def remove_team_member(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    raise NOT_IMPLEMENTED

@router.get("/fruit_teams/teams/{team_id}/{player_uuid}")
async def get_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@router.patch("/fruit_teams/teams/{team_id}/{player_uuid}/{points}")
async def set_team_member_points(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)],
    points: Annotated[int, Path(gt=0)]
):
    return NOT_IMPLEMENTED
    

# === Team Management ===

@router.post("/fruit_teams/teams/{team_id}")
async def create_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)],
    prefix: Annotated[str, Query(pattern=TEAM_PREFIX_REGEX)]
):
    return NOT_IMPLEMENTED

@router.get("/fruit_teams/random_team/{player_uuid}")
async def add_to_random_team(
    player_uuid: Annotated[str, Path(pattern=PLAYER_UUID_REGEX)]
):
    return NOT_IMPLEMENTED

@router.delete("/fruit_teams/teams/{team_id}")
async def delete_team(
    team_id: Annotated[str, Path(pattern=TEAM_ID_REGEX)]
):
    return NOT_IMPLEMENTED

# === Leaderboards ===

@router.get("/fruit_teams/leaderboard/top_10_teams")
async def get_top_10_teams():
    return NOT_IMPLEMENTED

@router.get("/fruit_teams/leaderboard/top_10_players")
async def get_top_10_players():
    return NOT_IMPLEMENTED
