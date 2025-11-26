from typing import List

from app.models.soldier import Soldier
from models.room import Room


class ResidentialBuilding:
    def __init__(self, building_num: int, rooms: List[Room] | None = None, rooms_amount: int = 10):
        if not rooms:
            rooms = []
        self.building_num = building_num
        self.rooms = rooms
        self.rooms_amount = rooms_amount

    def soldiers_amounts(self):
        return sum([room.soldiers_amount() for room in self.rooms])

    def add_soldier(self, new_soldier: Soldier):
        for room in self.rooms:
            if room.add_soldier(new_soldier):
                new_soldier.building_num = self.building_num
                return True
        return False

    def remove_soldier(self, soldier_num):
        for room in self.rooms:
            if room.remove_soldier(soldier_num):
                return True
        return False

    def get_rooms_info(self):
        full_rooms = len([room for room in self.rooms if room.is_full()])
        empty_rooms = len([room for room in self.rooms if room.is_empty()])
        partially_full_rooms = self.rooms_amount - (full_rooms + empty_rooms)
        rooms_info = {
            "full_rooms": full_rooms,
            "empty_rooms": empty_rooms,
            "partially_full_rooms": partially_full_rooms
        }
        return {
            "building_num": self.building_num,
            "rooms_info": rooms_info
        }

    @staticmethod
    def create_building(building_num):
        return ResidentialBuilding(building_num, Room.create_room_list())
