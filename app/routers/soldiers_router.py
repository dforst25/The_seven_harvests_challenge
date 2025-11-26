from fastapi import APIRouter

from routers.csv_handler import ARMY_BASE

router = APIRouter()


@router.get("/waitingList/")
def rooms_info():
    return [soldier.get_info() for soldier in ARMY_BASE.soldiers if not soldier.residential_assignment]
