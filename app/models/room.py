from models.soldier import Soldier


class Room:
    def __init__(self, room_num: int, soldiers=None, beds_amount: int = 8):
        if soldiers is None:
            soldiers = []
        self.room_num = room_num
        self.soldiers = soldiers
        self.bed_amount = beds_amount

    def soldiers_amount(self):
        return len(self.soldiers)

    def is_full(self):
        return self.soldiers_amount() == self.bed_amount

    def add_soldier(self, new_soldier: Soldier) -> bool:
        if self.is_full():
            return False
        else:
            self.soldiers.append(new_soldier)
            new_soldier.room_num = self.room_num
            return True

    def remove_soldier(self, soldier_num: int):
        amount_of_soldiers = len(self.soldiers)
        for i in range(amount_of_soldiers):
            if self.soldiers[i].personal_num == soldier_num:
                self.soldiers.pop(i)
                return True
        return False

    @staticmethod
    def create_room_list(size: int = 10):
        return [Room(i) for i in range(size)]
