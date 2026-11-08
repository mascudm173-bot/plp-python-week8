import random

def run_calculator():
    print("\n--- [Tool 1] Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ").strip()

        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print(f"Sorry, '{op}' is not a valid mathematical operation.")
    except ValueError:
        print("Invalid input! Please type numbers only.")

def run_guessing_game():
    print("\n--- [Tool 2] Number Guessing Game ---")
    print("I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Take a guess (1-20): "))
            attempts += 1

            if guess < secret_number:
                print(f"Too low! Try a higher number.")
            elif guess > secret_number:
                print(f"Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                guessed_correctly = True
        except ValueError:
            print("Please type a valid integer number.")

def run_task_organizer(tasks_list):
    print("\n--- [Tool 3] Task Organizer ---")
    print("1. View Current Tasks")
    print("2. Add a New Task")
    print("3. Clear Entire List")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        if not tasks_list:
            print("Your task list is currently empty!")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(tasks_list, start=1):
                print(f"  {index}. {task}")
    elif choice == "2":
        new_task = input("Enter the task description: ").strip()
        if new_task:
            tasks_list.append(new_task)
            print(f"Successfully added: '{new_task}'")
        else:
            print("Task description cannot be empty!")
    elif choice == "3":
        tasks_list.clear()
        print("All tasks have been completely cleared.")
    else:
        print("Invalid option selected inside the Task Organizer.")

def main():
    print("================================================")
    print("   Welcome to my Multi-Tool Interactive Toolkit!")
    print("================================================")
    
    my_tasks = []
    
    while True:
        print("\n--- PYTHON TOOLKIT MAIN MENU ---")
        print("1. Simple Calculator")
        print("2. Number Guessing Game")
        print("3. Task Organizer")
        print("4. Exit Toolkit")
        
        user_choice = input("Enter your selection (1-4): ").strip()
        
        if user_choice == "1":
            run_calculator()
        elif user_choice == "2":
            run_guessing_game()
        elif user_choice == "3":
            run_task_organizer(my_tasks)
        elif user_choice == "4":
            print("\nThank you for using the Toolkit. Goodbye!")
            break
        else:
            print(f"'{user_choice}' is not on the menu. Please enter a valid number (1-4).")

if __name__ == "__main__":
    main()
