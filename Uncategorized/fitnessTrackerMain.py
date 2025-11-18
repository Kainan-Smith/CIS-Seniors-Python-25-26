# UNSTRUCTURED PROGRAM - Needs fixing!
def welcome_msg():
    print("Fitness Tracker")
    print("===============")

def get_exercise():
    exercise = input("What exercise did you do? ")
    duration_str = input("How many minutes? ")
    duration = int(duration_str)
    return exercise, duration

def find_cals_per_min(duration):
    calories_per_minute = 8  # Average
    total_calories = duration * calories_per_minute
    return total_calories

def give_feedback(total_calories):
    if total_calories >= 300:
        feedback = "Great workout!"
    else:
        feedback = "Good start! Try for 30+ minutes next time."
    return feedback

def display_summary(exercise, duration, total_calories, feedback):
    print("\n\n---Summary---")
    print("Exercise: " + exercise)
    print("Duration: " + str(duration) + " minutes")
    print("Calories burned: " + str(total_calories))
    print(feedback)


def main():
    welcome_msg()

    exercise, duration = get_exercise()
    calsBurned = find_cals_per_min(duration)
    feedback = give_feedback(calsBurned)
    display_summary(exercise, duration, calsBurned, feedback)


if __name__ == "__main__":
    main()