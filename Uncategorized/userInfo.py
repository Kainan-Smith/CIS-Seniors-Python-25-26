def greet_user():
    '''Get user's name and greet them'''
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    return name

def get_age():
    '''Get and validate user's age'''
    age_str = input("How old are you? ")
    age = int(age_str)
    return age

def display_info(name, age):
    '''Display personalized information'''
    print("\n=== Your Profile ===")
    print("Name: " + name)
    print("Age: " + age)
    print("Grade Level: Senior")

def main():
    '''
    Main Function - controlls program flow
    '''
    print("Welcome to Profile Creator!")
    print("-" * 30)

    # Get Instructions
    user_name = greet_user()
    user_age = get_age()

    # Display results
    display_info(user_name, user_age)

    print("\nThank you for using Profile Creator!")

# Program entry point
if __name__ == "__main__":
    main()