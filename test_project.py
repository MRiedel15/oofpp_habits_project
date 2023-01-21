from analyse import list_of_all_habits
from habit import Habit
from db import get_db, add_habit, check_in_task, get_tracker_data, edit_habit, delete_habit


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")
        add_habit(self.db, "test_counter", "test_description", "weekly")
        add_habit(self.db, "test_habit", "test_habit_desc", "daily")
        check_in_task(self.db, "test_habit", "2022-12-22")
        check_in_task(self.db, "test_habit", "2022-12-23")
        check_in_task(self.db, "test_habit", "2022-12-25")
        check_in_task(self.db, "test_habit", "2022-12-26")
        check_in_task(self.db, "test_counter", "2022-12-26")


    def test_counter(self):
        counter = Habit("test_counter_1", "test_description_1", "weekly")
        counter.store(self.db)
        new_counter = Habit("test_counter_1", "test_desc", "daily")
        new_counter.edit(self.db)
        counter.add_event(self.db)
        new_counter.delete(self.db)

    def test_db_counter(self):
        data = get_tracker_data(self.db, "test_habit")
        assert len(data) == 4


    def teardown_method(self):
        self.db.close()
        import os
        os.remove("test.db")
