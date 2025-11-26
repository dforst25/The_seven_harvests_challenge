from fastapi import APIRouter

from models.base import Base as ArmyBase

from routers.csv_handler import ARMY_BASE

router = APIRouter()


@router.get("/space/")
def rooms_info():
    return [building.get_rooms_info() for building in ARMY_BASE.residential_buildings]
