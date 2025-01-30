#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlite3 import Date


def main():
    """ Main program """
    # Code goes over here.
    return 0

if __name__ == "__main__":
    main()
class Schedule:
    day: list["Day"]


class Day:
    date: Date
    starthour: int
    endhour: int
    number_of_persons_per_slot: int
    hours: list[int, list["Person"]]

class Person:
    name: str
    timetable: dict
    skills: list
    is_female: bool #TODO Think about the name of this
    friends: list["Person"]


class CreateNewSchedule():
    def init(self, data: dict, dayes: dict,):
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
    def check_if_one_person_is_female() -> bool:
        pass
    def check_if_every_skill_is_once_available() -> bool:
        pass