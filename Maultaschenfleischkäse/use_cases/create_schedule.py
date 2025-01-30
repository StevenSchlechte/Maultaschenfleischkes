from Maultaschenfleischkäse.dataclasses.day import Day
from Maultaschenfleischkäse.dataclasses.person import Person
from Maultaschenfleischkäse.dataclasses.schedule import Schedule


class CreateNewSchedule():
    def init(self, data: dict, dayes: dict):
        self.data = data

    def createSchedule() -> Schedule:
        pass
    
    def checkSchedule() -> bool:
        pass
    def check_if_slot_is_valid() -> bool:
        pass
    def check_if_everybody_gets_equaly_hours() -> bool:
        pass
    def check_if_everybody_gets_hours_with_friends() -> bool:
        pass
    def check_if_everybody_gets_only_hours_where_they_can() -> bool:
        pass

    def check_if_every_shift_has_one_female(self, day: Day) -> bool:
        for hour, person in day.hours:
            if not self.check_if_one_person_is_female(person):
                return False
        return True

    def check_if_one_person_is_female(persons: list[Person]) -> bool:
        for person in persons:
            if person.is_female == True:
                return True
        return False

    def check_if_every_skill_is_once_available() -> bool: #TODO Get List of Skills from SASA
        pass