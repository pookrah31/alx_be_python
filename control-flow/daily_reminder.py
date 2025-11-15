task = input("Enter your task: " )
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time bound? (yes/no): ").strip().lower()

# Using match-case to provide remainder based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"



if time_bound == "yes":
    message =f"Reminder: {message} that requires immmediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."
print(message)
     