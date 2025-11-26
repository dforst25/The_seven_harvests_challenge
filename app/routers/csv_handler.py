from fastapi import APIRouter
from fastapi import UploadFile
from utils.file_handler import upload_csv

from models.base import Base as ArmyBase
from models.soldier import Soldier

ARMY_BASE = ArmyBase.create_base()

router = APIRouter()


@router.post("/assignWithCsv/")
def upload_csv_router(file: UploadFile):
    header, rows = upload_csv(file)
    if header[0] in {"מספר אישי", "מספר חייל", "מספר_אישי", "מספר_חייל", "personal number", "personal_number"}:
        soldier_list = list(map(Soldier.from_list, rows))
        global ARMY_BASE
        ARMY_BASE.add_soldiers(soldier_list, "distance_from_base")
        quantity_placed = len(list(filter(lambda x: x.residential_assignment, soldier_list)))
        waiting_quantity = len(soldier_list) - quantity_placed
        soldiers_info = list(map(lambda x: x.get_info(), soldier_list))
        return {
            "summery": {"soldiers_who_were_placed": quantity_placed,
                        "soldiers_who_are_waiting": waiting_quantity},
            "soldiers": soldiers_info
        }
    else:
        return "Only supports soldier table"
