from db import get_tracker_data, get_habit_item, get_data_same_periodicity, get_periodicity_item, get_tracker_data_all
from datetime import datetime, timedelta


def list_of_all_habits(db):
    """
    to get a list of all habits incl. its values
    :param db: an initialized sqlite3 database connection
    :return:list of all habits and its values
    """
    list_of_counter = get_habit_item(db)
    counter_name_list = []
    # loop habit list
    for i in list_of_counter:
        counter_name_list.append({"name": i[0],
                                  "description": i[1],
                                  "periodicity": i[2]})
    return counter_name_list


def list_of_periodicity(db, periodicity):
    """
    to create list of habits with given periodicity
    :param db: an initialized sqlite3 database connection
    :param periodicity: given periodicity
    :return: a list of habits with same periodicity
    """
    period_list = get_data_same_periodicity(db, periodicity)
    hab_list = []
    for i in period_list:
        hab_list.append({"name": i[0],
                         "periodicity": i[2]})
    return hab_list


def create_single_tables(db):
    """
    to create single tracker tables for every habit
    :param db: an initialized sqlite3 database connection
    :return: single tracker table for every habit
    """
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


def longest_ever_streak(db):
    """
    to find the longest recorded streak
    :param db: an initialized sqlite3 database connection
    :return: the longest streak and its name of habit
    """
    tracker_lists = create_single_tables(db)
    # make list of keys from dictionary
    names_list = [key for key in tracker_lists.keys()]
    # loop names_list and set up results in high_streak_list
    high_streak_list = []
    x = 0
    while x < len(names_list):
        # get list of dates of actual habit
        dates_only = tracker_lists.get(names_list[x])
        nom = names_list[x]
        # get periodicity of actual habit
        period_1 = get_periodicity_item(db, nom)
        # string to datetime for calculation
        dates_datetime = [datetime.strptime(dates_only, "%Y-%m-%d") for dates_only in dates_only]
        # calculate streaks for current habit depending on daily or weekly
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
        else:
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=7):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
        x += 1
        list_of_streaks.sort(reverse=True)
        longest_streak = list_of_streaks  # [0]
        high_streak_list.append([nom, longest_streak])
    best_streak = max(high_streak_list, key=lambda x: x[1])
    res_1 = best_streak[0]
    res_2 = best_streak[1][0]
    return f"the longest streak is {res_2} from the habit: {res_1}"


def longest_run_streak(db, spec):
    """
    to find the longest streak of a specific habit
    :param db: an initialized sqlite3 database connection
    :param spec: specific habit name that is to be analysed
    :return: longest streak of specific habit
    """
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
        else:
            for i in range(1, len(dates_datetime)):
                if dates_datetime[i] - dates_datetime[i - 1] == timedelta(days=7):
                    my_streak += 1
                    list_of_streaks.append(my_streak)
                else:
                    my_streak = 1
                    continue
        list_of_streaks.sort(reverse=True)
        longest_streak = list_of_streaks[0]
        return longest_streak
    except:
        print("no streaks")
