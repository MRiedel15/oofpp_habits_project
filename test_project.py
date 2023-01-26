from analyse import list_of_all_habits, list_of_periodicity, longest_ever_streak, longest_run_streak
from habit import Habit
from db import get_db, add_habit, check_in_task, get_tracker_data, edit_habit, delete_habit


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")
        add_habit(self.db, "test_counter", "test_description", "weekly")
        add_habit(self.db, "test_habit", "test_habit_desc", "daily")
        check_in_task(self.db, "test_habit", "2022-12-22")
        check_in_task(self.db, "test_habit", "2022-12-23")
        edit_habit(self.db, "test_habit", "test_desc_habit", "weekly")
        check_in_task(self.db, "test_habit", "2022-12-25")
        check_in_task(self.db, "test_habit", "2022-12-26")
        check_in_task(self.db, "test_counter", "2022-12-26")
        delete_habit(self.db, "test_counter")
        test_habits = Habit("name", "description", "periodicity")
        test_habits.predefined_data(self.db)

    def test_counter(self):
        counter = Habit("test_counter_1", "test_description_1", "weekly")
        counter.store(self.db)
        new_counter = Habit("test_counter_2", "test_desc", "daily")
        new_counter.edit(self.db)
        counter.add_event(self.db)
        new_counter.delete(self.db)
        assert counter.name == "test_counter_1"

    def test_analysis_1(self):
        test_all_habits = list_of_all_habits(self.db)
        assert len(test_all_habits) == 6

    def test_analysis_2(self):
        test_periodicity_list_w = list_of_periodicity(self.db, "weekly")
        test_periodicity_list_d = list_of_periodicity(self.db, "daily")
        assert len(test_periodicity_list_w) == 2, len(test_periodicity_list_d) == 4

    def test_analysis_3(self):
        test_longest_streak = longest_ever_streak(self.db)
        assert test_longest_streak == 'the longest streak is 9 from the habit: Drinking water'

    def test_analysis_4(self):
        test_long_spec = longest_run_streak(self.db, "Good-night-sleep")
        assert test_long_spec == 8

    def test_db_counter(self):
        data = get_tracker_data(self.db, "Read a book")
        assert len(data) == 3

    def teardown_method(self):
        self.db.close()
        import os
        os.remove("test.db")
