def timer():
    print("timer")
def task_list():
    def todo_editor():
        print("Ok lets Get started")
        

    tasks = [1, 2, 3]
    print("To-Do", *tasks, sep="\n")
    edit_tasks = input("would you like to edit your list?")
    if edit_tasks == "y":
        todo_editor()
    elif edit_tasks == "n":
        print("Ok sounds good")
        print("To-Do", *tasks, sep="\n")

    
def daily_schedule():
    print("placeholder")
def weekly_schedule():
    print("placeholder")
def options():
    user_input = input('''How can I help you today? 
    1.Pomodoro Timer
    2.Task List
    3.Daily Schedule
    4.Week Schedule
    ''')
    if user_input == "1":
        timer()
    elif user_input == "2":
        task_list()
    elif user_input == "3":
        daily()
    elif user_input == "4":
        week()
    else:
        print("invalid input try again")
        options()


def main():
    print("Welcome to the Pomodoro Organizer!")
    options()
main()