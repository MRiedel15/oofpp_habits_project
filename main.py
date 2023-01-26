import questionary

from habit import Habit
from db import get_db
from analyse import list_of_all_habits, list_of_periodicity, longest_run_streak, longest_ever_streak


def cli():
    db = get_db()
    # questionary.confirm("Are you ready?").ask()

    habit_list = list_of_all_habits(db)

    stop = False
    while not stop:
        choice = questionary.select(
            "Welcome. What do you like to do?",
            choices=["Manage my habits", "Check in a completed task", "Analyse my habits", "Exit"]
        ).ask()

        if choice == "Manage my habits":
            manage = questionary.select(
                "What would you like to do?",
                choices=["create a new habit", "edit an existing habit", "delete an existing habit",
                         "load predefined data"]
            ).ask()

            if manage == "create a new habit":
                name = questionary.text("What is the name of your new habit?").ask()
                desc = questionary.text("What is the description of your habit?").ask()
                per = questionary.select(
                    "What is the periodicity?",
                    choices=["daily", "weekly"]
                ).ask()
                counter = Habit(name, desc, per)
                counter.store(db)

            elif manage == "edit an existing habit":
                name = questionary.select(
                    "Which habit would like to edit?",
                    choices=habit_list
                ).ask()

                desc = questionary.text("What is the new description of your habit").ask()
                per = questionary.select(
                    "What is the new periodicity?",
                    choices=["daily", "weekly"]
                ).ask()
                counter = Habit(name, desc, per)
                counter.edit(db)

            elif manage == "delete an existing habit":
                counter_item_delete = questionary.select(
                    "Which habit would like to delete?",
                    choices=habit_list
                ).ask()

                counter = Habit(counter_item_delete, "No description", "default")
                counter.delete(db)
            elif manage == "load predefined data":
                counter = Habit("name", "description", "periodicity")
                counter.predefined_data(db)


        elif choice == "Check in a completed task":
            counter_item_current = questionary.select(
                "Which task did you complete today?",
                choices=habit_list
            ).ask()

            counter = Habit(counter_item_current, "No description", "default")
            # counter.increment()
            counter.add_event(db)
        elif choice == "Analyse my habits":
            analyse = questionary.select(
                "What would you like to analyse?",
                choices=["list of all tracked habits",
                         "list of all with same periodicity",
                         "habit with the longest run streak",
                         "longest run streak for a specific habit"]
            ).ask()
            if analyse == "list of all tracked habits":
                print("Here is a list of your currently tracked habits:", habit_list)

            elif analyse == "list of all with same periodicity":
                period = questionary.select(
                    "For which periodicity would you like to see your habits?",
                    choices=["daily", "weekly"]
                ).ask()
                period_list = list_of_periodicity(db, period)

                print("Here is a list of your ", period, " habits!:", period_list)

            elif analyse == "habit with the longest run streak":
                print(longest_ever_streak(db))


            elif analyse == "longest run streak for a specific habit":
                spec = questionary.select(
                    "For which habit would you like to know your longest run streak?",
                    choices=habit_list
                ).ask()
                high_str = longest_run_streak(db, spec)
                print("longest streak of", spec, "is :", high_str)

        else:
            print("Bye!")
            stop = True


if __name__ == "__main__":
    cli()
