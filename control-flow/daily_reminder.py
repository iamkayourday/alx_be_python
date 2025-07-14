# Personal Daily Reminder
# This program reminds you t

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority not in ['high', 'medium', 'low']:
    print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
else:
    if time_bound not in ['yes', 'no']:
        print("Invalid response for time-bound. Please enter 'yes' or 'no'.")
    else:
        match priority:
            case 'high':
                print(f"Reminder: {task} is high priority task that requires immediate attention today.")
            case 'medium':
                print(f"Reminder: {task} is a medium priority task that should be completed soon.")
            case 'low':
                print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
            case _:
                print("Invalid priority level. Please enter high, medium, or low.")

