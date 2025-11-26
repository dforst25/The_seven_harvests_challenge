from typing import List
from operator import attrgetter
from app.models.soldier import Soldier
from models.residential_buildings import ResidentialBuilding


class Base:
    def __init__(self, residential_buildings: List[ResidentialBuilding] | None = None,
                 residential_buildings_amount: int = 2):
        if not residential_buildings:
            residential_buildings = []
        self.residential_buildings = residential_buildings
        self.residential_buildings_amount = residential_buildings_amount
        self.soldiers = []

    def soldiers_amounts(self):
        return sum([residential_building.soldiers_amount() for residential_building in self.residential_buildings])

    def add_soldier(self, new_soldier: Soldier):
        self.soldiers.append(new_soldier)
        for residential_building in self.residential_buildings:
            if residential_building.add_soldier(new_soldier):
                return True
        return False

    def add_soldiers(self, soldiers: List[Soldier], field: str, desc: bool = True):
        sorted_soldiers = sorted(soldiers, key=attrgetter(field), reverse=desc)
        soldiers_amount = len(sorted_soldiers)
        for i in range(soldiers_amount):
            if self.add_soldier(sorted_soldiers[i]):
                sorted_soldiers[i].residential_assignment = True
        return False

    @staticmethod
    def create_base():
        return Base([ResidentialBuilding.create_building(1), ResidentialBuilding.create_building(2)])
