Task = input("Enter your task: " )
Priority = input("Priority (high/medium/low): ").strip().lower()
TimeBound = input("Is it time bound? (yes/no): ").strip().lower()

# Using match-case to provide remainder based on priority
match Priority:
    case "high":
        message = f"'{Task}' is a high priority task"
    case "medium":
        message = f"'{Task}' is a medium priority task"
    case "low":
        message = f"'{Task}' is a low priority task"
    case _:
        message = f"'{Task}' has an undefined priority"



if TimeBound == "yes":
    message =f"Reminder: {message} that requires immmediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."
print(message)
     