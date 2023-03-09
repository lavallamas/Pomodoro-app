
def main():
    print("Welcome to the Pomodoro Organizer!")
    options()
main()
def options():
    input('''How can I help you today? 
    1.Pomodoro Timer
    2.Task List
    3.Daily Schedule
    4.Week Schedule
    ''')
    if input == 1:
        timer()
    elif input == 2:
        task()
    elif input == 3:
        daily()
    elif input == 4:
        week()
    else:
        print("invalid input try again")
        options()
