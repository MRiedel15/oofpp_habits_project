from db import add_habit, check_in_task, edit_habit, delete_habit


class Habit:

    def __init__(self, name: str, description: str, periodicity: str):
        """
        Habit class to manage the habits in the project.
        :param name: name of the habit
        :param description: description of the habit
        :param periodicity: periodicity
        """
        self.name = name
        self.description = description
        self.periodicity = periodicity

    def store(self, db):
        """
        to create a new habits in the database
        :param db: an initialized sqlite3 database connection
        :return: database entry
        """
        add_habit(db, self.name, self.description, self.periodicity)

    def add_event(self, db, date: str = None):
        """
        to check in a task
        :param db: an initialized sqlite3 database connection
        :param date: data to be entered
        :return: database entry
        """
        check_in_task(db, self.name, date)

    def edit(self, db):
        """
        to edit a existing habit
        :param db: an initialized sqlite3 database connection
        :return: change of data
        """
        edit_habit(db, self.name, self.description, self.periodicity)

    def delete(self, db):
        """
        to delete a existing habit
        :param db: an initialized sqlite3 database connection
        :return: data deleted
        """
        delete_habit(db, self.name)
