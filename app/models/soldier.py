class Soldier:
    def __init__(self, personal_num: int, first_name: str, last_name: str, sex: str, city: str,
                 distance_from_base: int, residential_assignment: bool = False, room_num: int | None = None, building_num: int | None = None ):
        self.personal_num = int(personal_num)
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.city = city
        self.distance_from_base = int(distance_from_base)
        self.residential_assignment = residential_assignment
        self.room_num = room_num
        self.building_num = building_num

    def to_dict(self):
        return self.__dict__

    def get_info(self):
        info = {"name": self.first_name + '_' + self.last_name,
                "personal_num": self.personal_num,
                "placed": self.residential_assignment}
        if info["placed"]:
            info["room_num"] = self.room_num
            info["building_num"] = self.building_num
        return info

    @staticmethod
    def from_list(soldier_list: dict) -> "Soldier":
        if len(soldier_list) != 6:
            raise AttributeError("No match for a soldier!")
        return Soldier(*tuple(soldier_list))


