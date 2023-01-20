import sqlite3
from datetime import date


def get_db(name="main.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT PRIMARY KEY,
        description TEXT,
        periodicity TEXT)""")

    for elem in init_counter_list:
        add_counter(db, elem[0], elem[1], elem[2])

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        counterName TEXT,
        FOREIGN KEY (counterName) REFERENCES counter(Name),
        UNIQUE(date, counterName))""")
    db.commit()

    for elem in init_sleep_tracker_list:
        increment_counter(db, elem[0], elem[1])

    for elem in init_water_tracker_list:
        increment_counter(db, elem[0], elem[1])

    for elem in init_work_out_list:
        increment_counter(db, elem[0], elem[1])

    for elem in init_meals_tracker_list:
        increment_counter(db, elem[0], elem[1])

    for elem in init_read_tracker:
        increment_counter(db, elem[0], elem[1])


def add_counter(db, name, description, periodicity):
    cur = db.cursor()
    cur.execute("INSERT OR REPLACE INTO counter VALUES(?, ?, ?)", (name, description, periodicity))
    db.commit()


def increment_counter(db, name, event_date=None):
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute("INSERT OR REPLACE INTO tracker VALUES(?, ?)", (event_date, name))
    db.commit()


def get_tracker_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE counterName=?", (name,))
    return cur.fetchall()


def get_tracker_streak_data(db):
    streak = "SELECT * FROM tracker"
    cur = db.cursor()
    cur.execute(streak)
    return cur.fetchall()


def get_counter_item(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM counter")
    return cur.fetchall()


def get_periodicity_item(db, name):
    cur = db.cursor()
    cur.execute("SELECT periodicity FROM counter WHERE name=?", (name,))
    return cur.fetchall()


def get_data_same_periodicity(db, periodicity):
    period_type = "SELECT * FROM counter WHERE periodicity = ?"
    cur = db.cursor()
    cur.execute(period_type, (periodicity,))
    return cur.fetchall()


def get_tracker_data_all(db):
    cur = db.cursor()
    cur.execute("SELECT counterName, date FROM tracker")
    return cur.fetchall()

    #for name in name_lists:
        #new_list = name_lists[name]
        #print(new_list)



def edit_habit(db, name, description, periodicity):
    edit = """UPDATE counter SET description = ? , periodicity = ? where name = ?"""
    cur = db.cursor()
    cur.execute(edit, (name, description, periodicity))
    db.commit()


def delete_habit(db, name):
    delete_counter = "DELETE FROM counter WHERE name = ?"
    cur = db.cursor()
    cur.execute(delete_counter, (name,))
    db.commit()


init_counter_list = [
    ("Good-night-sleep", "get more than 8 hours of sleep", "daily"),
    ("Drinking water", "drink at least 2 liters of water a day", "daily"),
    ("Meals", "have at least 3 meals a day", "daily"),
    ("Work out time", "work out at least 30 min a day", "daily"),
    ("Read a book", "read a book at least 2 hours a week", "weekly")
]

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

init_water_tracker_list = [
    ("Drinking water", "2022-12-01"), ("Drinking water", "2022-12-02"), ("Drinking water", "2022-12-03"),
    ("Drinking water", "2022-12-04"), ("Drinking water", "2022-12-07"), ("Drinking water", "2022-12-08"),
    ("Drinking water", "2022-12-10"), ("Drinking water", "2022-12-11"), ("Drinking water", "2022-12-14"),
    ("Drinking water", "2022-12-16"), ("Drinking water", "2022-12-18"), ("Drinking water", "2022-12-22"),
    ("Drinking water", "2022-12-23"), ("Drinking water", "2022-12-24"), ("Drinking water", "2022-12-25"),
    ("Drinking water", "2022-12-26"), ("Drinking water", "2022-12-27"), ("Drinking water", "2022-12-28"),
    ("Drinking water", "2022-12-29"), ("Drinking water", "2022-12-30")
]

init_meals_tracker_list = [
    ("Meals", "2022-12-01"), ("Meals", "2022-12-02"), ("Meals", "2022-12-04"), ("Meals", "2022-12-06"),
    ("Meals", "2022-12-08"), ("Meals", "2022-12-10"), ("Meals", "2022-12-11"), ("Meals", "2022-12-12"),
    ("Meals", "2022-12-13"), ("Meals", "2022-12-16"), ("Meals", "2022-12-18"), ("Meals", "2022-12-19"),
    ("Meals", "2022-12-20"), ("Meals", "2022-12-24"), ("Meals", "2022-12-26"), ("Meals", "2022-12-28"),
    ("Meals", "2022-12-29")
]

init_work_out_list = [
    ("Work out time", "2022-12-01"), ("Work out time", "2022-12-02"), ("Work out time", "2022-12-03"),
    ("Work out time", "2022-12-04"), ("Work out time", "2022-12-05"), ("Work out time", "2022-12-06"),
    ("Work out time", "2022-12-07"), ("Work out time", "2022-12-10"), ("Work out time", "2022-12-11"),
    ("Work out time", "2022-12-12"), ("Work out time", "2022-12-13"), ("Work out time", "2022-12-18"),
    ("Work out time", "2022-12-19"), ("Work out time", "2022-12-20"), ("Work out time", "2022-12-21"),
    ("Work out time", "2022-12-22"), ("Work out time", "2022-12-27")
]

init_read_tracker = [
    ("Read a book", "2022-12-01"), ("Read a book", "2022-12-08"), ("Read a book", "2022-12-27")
]
