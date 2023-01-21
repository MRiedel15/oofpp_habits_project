import sqlite3
from datetime import date


def get_db(name="main.db"):
    """
    to connect to database
    :param name: name of the database
    :return: database connection
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """
    to create tables and predefine habit data
    :param db: an initialized sqlite3 database connection
    :return: tables are created and predefined habit data is entered
    """
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS habits (
        name TEXT PRIMARY KEY,
        description TEXT,
        periodicity TEXT)""")

    for elem in init_counter_list:
        add_habit(db, elem[0], elem[1], elem[2])

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        habitsName TEXT,
        FOREIGN KEY (habitsName) REFERENCES habits(Name),
        UNIQUE(date, habitsName))""")
    db.commit()

    for elem in init_sleep_tracker_list:
        check_in_task(db, elem[0], elem[1])

    for elem in init_water_tracker_list:
        check_in_task(db, elem[0], elem[1])

    for elem in init_work_out_list:
        check_in_task(db, elem[0], elem[1])

    for elem in init_meals_tracker_list:
        check_in_task(db, elem[0], elem[1])

    for elem in init_read_tracker:
        check_in_task(db, elem[0], elem[1])


def add_habit(db, name, description, periodicity):
    """
    to enter new habit data habits table
    :param db: an initialized sqlite3 database connection
    :param name: name of habit
    :param description: description of habit
    :param periodicity: periodicity of habit
    :return: database entry of new habit
    """
    cur = db.cursor()
    cur.execute("INSERT OR REPLACE INTO habits VALUES(?, ?, ?)", (name, description, periodicity))
    db.commit()


def check_in_task(db, name, event_date=None):
    """
    to enter check-in-task-data to database
    :param db: an initialized sqlite3 database connection
    :param name: name of habit that is to be checked in
    :param event_date: date of (today) checked in habit
    :return: data entry of completed task today
    """
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute("INSERT OR REPLACE INTO tracker VALUES(?, ?)", (event_date, name))
    db.commit()


def get_tracker_data(db, name):
    """
    to access tracker table
    :param db: an initialized sqlite3 database connection
    :param name: name of habit that is searched for
    :return: entered data of specific data
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE habitsName=?", (name,))
    return cur.fetchall()


def get_tracker_streak_data(db):
    """
    to get all data from tracker table
    :param db: an initialized sqlite3 database connection
    :return: tracker table
    """
    streak = "SELECT * FROM tracker"
    cur = db.cursor()
    cur.execute(streak)
    return cur.fetchall()


def get_habit_item(db):
    """
    to get all data from habits table
    :param db: an initialized sqlite3 database connection
    :return: habits table
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habits")
    return cur.fetchall()


def get_periodicity_item(db, name):
    """
    to get periodicity of single habit name
    :param db: an initialized sqlite3 database connection
    :param name: name of habit to find out periodicity
    :return: periodicity of specific habit
    """
    cur = db.cursor()
    cur.execute("SELECT periodicity FROM habits WHERE name=?", (name,))
    return cur.fetchall()


def get_data_same_periodicity(db, periodicity):
    """
    to get data of all habits with same periodicity
    :param db: an initialized sqlite3 database connection
    :param periodicity: specific periodicity to find linked habits
    :return: habits with specific periodicity
    """
    period_type = "SELECT * FROM habits WHERE periodicity = ?"
    cur = db.cursor()
    cur.execute(period_type, (periodicity,))
    return cur.fetchall()


def get_tracker_data_all(db):
    """
    to get name and dates from tracker table
    :param db: an initialized sqlite3 database connection
    :return: tracker table with all names and dates
    """
    cur = db.cursor()
    cur.execute("SELECT habitsName, date FROM tracker")
    return cur.fetchall()


def edit_habit(db, name, description, periodicity):
    """
    to edit data in habits table
    :param db: an initialized sqlite3 database connection
    :param name: name of habit to be edited
    :param description: new description of habit
    :param periodicity: new periodicity of habit
    :return: habit with new description and periodicity
    """
    edit = """UPDATE habits SET description = ? , periodicity = ? where name = ?"""
    cur = db.cursor()
    cur.execute(edit, (name, description, periodicity))
    db.commit()


def delete_habit(db, name):
    """
    to delete data (habit) from habits table
    :param db: an initialized sqlite3 database connection
    :param name: name of habit to be deleted
    :return: deleted habit
    """
    delete_counter = "DELETE FROM habits WHERE name = ?"
    cur = db.cursor()
    cur.execute(delete_counter, (name,))
    db.commit()


# predefined habit table = 5 habits (at least 1 daily and at least 1 weekly)
init_counter_list = [
    ("Good-night-sleep", "get more than 8 hours of sleep", "daily"),
    ("Drinking water", "drink at least 2 liters of water a day", "daily"),
    ("Meals", "have at least 3 meals a day", "daily"),
    ("Work out time", "work out at least 30 min a day", "daily"),
    ("Read a book", "read a book at least 2 hours a week", "weekly")
]

# predefined tracker table of the 5 predefined habits (at least 4 weeks of data)
# Good-night-sleep (daily)
init_sleep_tracker_list = [
    ("Good-night-sleep", "2022-12-01"), ("Good-night-sleep", "2022-12-02"), ("Good-night-sleep", "2022-12-03"),
    ("Good-night-sleep", "2022-12-04"), ("Good-night-sleep", "2022-12-05"), ("Good-night-sleep", "2022-12-06"),
    ("Good-night-sleep", "2022-12-07"), ("Good-night-sleep", "2022-12-08"), ("Good-night-sleep", "2022-12-10"),
    ("Good-night-sleep", "2022-12-12"), ("Good-night-sleep", "2022-12-13"), ("Good-night-sleep", "2022-12-14"),
    ("Good-night-sleep", "2022-12-15"), ("Good-night-sleep", "2022-12-16"), ("Good-night-sleep", "2022-12-17"),
    ("Good-night-sleep", "2022-12-18"), ("Good-night-sleep", "2022-12-20"), ("Good-night-sleep", "2022-12-24"),
    ("Good-night-sleep", "2022-12-25"), ("Good-night-sleep", "2022-12-27"), ("Good-night-sleep", "2022-12-28"),
    ("Good-night-sleep", "2022-12-29"), ("Good-night-sleep", "2022-12-30"), ("Good-night-sleep", "2022-12-31"),
]

# Drinking water (daily)
init_water_tracker_list = [
    ("Drinking water", "2022-12-01"), ("Drinking water", "2022-12-02"), ("Drinking water", "2022-12-03"),
    ("Drinking water", "2022-12-04"), ("Drinking water", "2022-12-07"), ("Drinking water", "2022-12-08"),
    ("Drinking water", "2022-12-10"), ("Drinking water", "2022-12-11"), ("Drinking water", "2022-12-14"),
    ("Drinking water", "2022-12-16"), ("Drinking water", "2022-12-18"), ("Drinking water", "2022-12-22"),
    ("Drinking water", "2022-12-23"), ("Drinking water", "2022-12-24"), ("Drinking water", "2022-12-25"),
    ("Drinking water", "2022-12-26"), ("Drinking water", "2022-12-27"), ("Drinking water", "2022-12-28"),
    ("Drinking water", "2022-12-29"), ("Drinking water", "2022-12-30")
]

# Meals (daily)
init_meals_tracker_list = [
    ("Meals", "2022-12-01"), ("Meals", "2022-12-02"), ("Meals", "2022-12-04"), ("Meals", "2022-12-06"),
    ("Meals", "2022-12-08"), ("Meals", "2022-12-10"), ("Meals", "2022-12-11"), ("Meals", "2022-12-12"),
    ("Meals", "2022-12-13"), ("Meals", "2022-12-16"), ("Meals", "2022-12-18"), ("Meals", "2022-12-19"),
    ("Meals", "2022-12-20"), ("Meals", "2022-12-24"), ("Meals", "2022-12-26"), ("Meals", "2022-12-28"),
    ("Meals", "2022-12-29")
]

# Work out time (daily)
init_work_out_list = [
    ("Work out time", "2022-12-01"), ("Work out time", "2022-12-02"), ("Work out time", "2022-12-03"),
    ("Work out time", "2022-12-04"), ("Work out time", "2022-12-05"), ("Work out time", "2022-12-06"),
    ("Work out time", "2022-12-07"), ("Work out time", "2022-12-10"), ("Work out time", "2022-12-11"),
    ("Work out time", "2022-12-12"), ("Work out time", "2022-12-13"), ("Work out time", "2022-12-18"),
    ("Work out time", "2022-12-19"), ("Work out time", "2022-12-20"), ("Work out time", "2022-12-21"),
    ("Work out time", "2022-12-22"), ("Work out time", "2022-12-27")
]

# Read a bool (weekly)
init_read_tracker = [
    ("Read a book", "2022-12-01"), ("Read a book", "2022-12-08"), ("Read a book", "2022-12-27")
]
