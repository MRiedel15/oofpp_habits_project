from db import add_counter, increment_counter, edit_habit, delete_habit


class Counter:

    def __init__(self, name: str, description: str, periodicity: str):
        """
        Counter class to count the events.
        :param name: name of the counter
        :param description: description of the counter
        """
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.count = 0

    #def increment(self):
        self.count += 1

    #def reset(self):
        self.count = 0

    #def __str__(self):
        #return f"{self.name}: {self.count}"

    def store(self, db):
        add_counter(db, self.name, self.description, self.periodicity)

    def add_event(self, db, date: str = None):
        increment_counter(db, self.name, date)

    def edit(self, db):
        edit_habit(db, self.name, self.description, self.periodicity)

    def delete(self, db):
        delete_habit(db, self.name)






