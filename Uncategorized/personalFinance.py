'''
Personal Finance Manager
Program: personalFinance.py
Author: David Wells
Date: 11/28/2025

This program demonstrates proper Python program structure using a main() function and helper functions to coordinate program flow.
'''

def display_header():
    '''
    Display the program header and welcome message.

    This function has no parameters and returns nothing.
    It's purely for display purposes.
    '''
    print("\n\n\n")
    print("=" * 50)
    print("                 PERSONAL FINCANCE MANAGER")
    print("                 Plan Your College Budget!")
    print("=" * 50)
    print()

def get_user_name():
    '''
    Get the user's name

    Returns:
        name (str): The user's name

    NOTE: We use a separate function for this to keep each function doing ONE specific task
    '''
    name = input("What is your nae? ")
    return name

def get_income():
    '''
    Get an return the user's monthly income

    Returns:
        income (float): Monthly income in USD

    NOTE: We convert to a float to handle decimal values and to enable mathematical operations
    '''
    print("\nEnter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income

def get_expenses():
    '''
    Collect all expense categories from the user

    Returns:
        expenses_dict (dict): Dictionary with expense categories
        total_expenses (float): Sum of all expenses

    NOTE: This function demonstrates collecting multiple related inputs and organizing them in a dictionary for easy access later.
    '''
    print("\n--- EXPENSE TRACKING ---")

    # Dictionary to store all expenses
    expenses = {}

    # Get each expense category
    print("Enter your rent/housing cost: $", end="")
    expenses["Rent/Housing"] = float(input())

    print("Enter your food/grocery budget: $", end="")
    expenses["Food/Groceries"] = float(input())

    print("Enter your transportation costs: $", end="")
    expenses["Transportation"] = float(input())

    print("Enter your entertainment budget: $", end="")
    expenses["Entertainment"] = float(input())

    print("Enter your savings goal: $", end="")
    expenses["Savings"] = float(input())

    print("Enter miscellaneous expenses: $", end="")
    expenses["Miscellaneous"] = float(input())

    # Calculate total expenses
    total = sum(expenses.values())

    # Return both the dictionary and the total
    return expenses, total


def calculate_remaining(income, expenses):
    pass

def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    pass

def main():
    '''
    Main Function -coordinates the entire program

    Notice how main() reads like a story:
    1. Display header
    2. Get user information
    3. Get expenses
    4. Calculate results
    5. Get feedback
    6. Display summary
    7. Say goodbye

    Every step is one function call, making the logic easy to follow.
    '''

    # 1. Display Welcome
    display_header()
    print("Welcome!  Let's track your monthly finances.\n")

    # 2. Get User Information
    user_name = get_user_name()
    monthly_income = get_income()

    # 3. Get expense information
    # NOTE: This function returns TWO values (tuple unpacking)
    expense_categories, total_expenses = get_expenses()

    # 4. Calculate results

    # 5. Get feedback

    # 6. Display summary

    # 7. Say goodbye

if __name__ == "__main__":
    main()