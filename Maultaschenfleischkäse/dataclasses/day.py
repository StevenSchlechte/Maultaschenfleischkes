from sqlite3 import Date

from Maultaschenfleischkäse.dataclasses.person import Person


class Day:
    date: Date
    starthour: int
    endhour: int
    number_of_persons_per_slot: int
    hours: list[int, list["Person"]]