from db import get_tracker_data, get_counter_item, get_data_same_periodicity, get_periodicity_item, get_tracker_data_all
from datetime import datetime, timedelta


def calculate_count(db, counter):
    """
    calculate the count of the counter.
    :param db: an initialized sqlite3 database connection.
    :param counter:name of the counter present in the db.
    :return: length of the counter increment events
    """
    data = get_tracker_data(db, counter)
    return len(data)


def list_of_all_habits(db):
    list_of_counter = get_counter_item(db)
    counter_name_list = []
    # loop counter list
    for i in list_of_counter:
        counter_name_list.append({"name": i[0],
                                  "description": i[1],
                                  "periodicity": i[2]})
    return counter_name_list


def list_of_periodicity(db, periodicity):
    period_list = get_data_same_periodicity(db, periodicity)
    hab_list = []
    for i in period_list:
        hab_list.append({"name": i[0],
                         "periodicity": i[2]})
    return hab_list


def create_single_tables(db):
    # sort tracker data by name
    res = get_tracker_data_all(db)
    name_lists = {}
    for row in res:
        nam = row[0]
        date = row[1]
        if nam not in name_lists:
            name_lists[nam] = []
        name_lists[nam].append(date)
    return name_lists


def list_of_names_tracker(db):
    trackname = create_single_tables(db)
    w = trackname.get("Read a book")
    x = trackname.keys()
    key_list = [key for key in x]
    r = key_list[0]
    period_1 = get_periodicity_item(db, "Read a book")
    list_of_mist = [i[0] for i in period_1]
    return list_of_mist


def list_of_all_names(db):
    # get list of all names
    hab_list = list_of_all_habits(db)
    names_list = [a['name'] for a in hab_list]
    return names_list


def longest_ever_streak(db):
    tracker_lists = create_single_tables(db)
    names_list = [key for key in tracker_lists.keys()]

    high_streak_list = []
    x = 0
    while x < len(names_list):
        dates_only = tracker_lists.get(names_list[x])
        nom = names_list[x]
        period_1 = get_periodicity_item(db, nom)
        dates_datetime = [datetime.strptime(dates_only, "%Y-%m-%d") for dates_only in dates_only]
        list_of_streaks = []
        my_streak = 1
        if period_1 == [("daily",)]:
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=1):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
                # error if no streaks
        else:
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=7):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
                # error if no streaks
        x += 1
        list_of_streaks.sort(reverse=True)
        longest_streak = list_of_streaks#[0]
        high_streak_list.append([nom, longest_streak])
    best_streak = max(high_streak_list, key=lambda x:x[1])
    res_1 = best_streak[0]
    res_2 = best_streak[1][0]
    return f"the longest streak is {res_2} from the habit: {res_1}"


def longest_run_streak(db, spec):
    track_list = get_tracker_data(db, spec)
    dates_only = [x[0] for x in track_list]

    dates_datetime = [datetime.strptime(dates_only, "%Y-%m-%d") for dates_only in dates_only]
    period_1 = get_periodicity_item(db, spec)[0][0]
    try:
        list_of_streaks = []
        my_streak = 1
        if period_1 == "daily":
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=1):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
                # error if no streaks
        else:
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=7):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
                # error if no streaks
        list_of_streaks.sort(reverse=True)
        longest_streak = list_of_streaks[0]
        return longest_streak
    except:
        print("no streaks")
