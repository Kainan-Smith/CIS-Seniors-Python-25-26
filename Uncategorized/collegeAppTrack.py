def get_sat_score():
    score = int(input("What did you get on your SAT? "))
    
    return score


def get_college_count():
    count = int(input("How many colleges are you applying to? "))
    return count


def get_application_cost(colleges):
    cost = colleges * 50
    return cost


def display_welcome():
    '''
    Display welcome banner
    '''
    name = input("What is your name? ")
    print("Hello " + name + "!")


def analyze_sat(score):
    '''
    Provide feedback on SAT score
    >= 1400 - Excellent
    >= 1200 - Good score
    >= 1000 - Solid foundation
    else - consider retaking to improve college options
    '''
    if score >= 1400:
        feedback = "Excellent!"
    elif score >= 1200:
        feedback = "Good score!"
    elif score >= 1000:
        feedback = "Solid foundation!"
    elif score < 1000:
        feedback = "Consider retaking to improve college options."
    return feedback


def display_summary(colleges, cost, sat_score, sat_feedback):
    '''
    Display complete application summary
    '''
    print("It will cost $" + str(cost) + " to apply to all " + str(colleges) + " colleges.")
    print("You got a " + str(sat_score) + " on your SAT, " + str(sat_feedback))


def main():
    '''Main Function - orchestrates the entire program'''
    # Welcome the user
    display_welcome()

    # Collect information
    num_colleges = get_college_count()
    total_cost = get_application_cost(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)

    print("\nGood luck with your applications")

if __name__ == "__main__":
     main()