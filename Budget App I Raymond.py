class BudgetApp:
    def __init__(self):
        self.income = 0.0
        self.user_goal = 0.0
        self.expenses = {
            "Housing": 0.0,
            "Food": 0.0,
            "Transportation": 0.0,
            "Entertainment": 0.0,
            "Other": 0.0
        }

    def safe_input(self, prompt, max_length=100):
        user_input = input(prompt)
        if len(user_input) > max_length:
            print("Input too long — please keep responses reasonable.")
            return self.safe_input(prompt, max_length)
        return user_input.strip()
        
        
    def set_user_income(self):
        self.income = self.get_and_validate_float("What's your monthly income? ", allow_zero=False)
        print(f"Income set to ${self.income:.2f}\n")
        
        

    def view_balance(self):
        remaining = self.income - sum(self.expenses.values())
        print(f"\nYour leftover cash after expenses is: ${remaining:.2f}\n")
        
        

    def add_expense(self):
        print("\nExpenses:")
        for i, category in enumerate(self.expenses.keys(), 1):
            print(f"{i}. {category}")

        while True:
            try:
                choice = int(input("Choose a category number: "))
                if 1 <= choice <= len(self.expenses):
                    category = list(self.expenses.keys())[choice - 1]
                    break
                else:
                    print("Please choose a valid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        amount = self.get_and_validate_float(f"Enter monthly amount for {category}: ")
        self.expenses[category] += amount
        print(f"Added ${amount:.2f} to {category}.\n")

    def view_summary(self):
        print("\nSummary of your budget:")
        total_expenses = sum(self.expenses.values())
        print(f"Your total income:     ${self.income:.2f}")
        print(f"Your total:   ${total_expenses:.2f}")
        print(f"Your lefover cash after subtracting your income by expenses:${self.income - total_expenses:.2f}")
        print("\nExpenses by Category:")
        for cat, amount in self.expenses.items():
            percent = (amount / self.income * 100) if self.income > 0 else 0
            print(f"  {cat}: ${amount:.2f} ({percent:.1f}%)")
        print("--------------------------\n")

    def set_savings_goal(self):
        goal = self.get_and_validate_float("Enter your savings goal: ")
        remaining = self.income - sum(self.expenses.values())
        print(f"\nYou have ${remaining:.2f} remaining after expenses.")
        if remaining >= (goal+10000):
            print("Good luck with that!  It's possible.  You've got some savings to do.")
        elif remaining > goal:
            print("Your goal is reasonable")
        else:
            print("This goal isn't feasible because you don't have enough money left over after subtracting expenses.")
        self.user_goal = goal
        print()


    def get_and_validate_float(self, prompt, allow_zero=False):
        while True:
            try:
                value_str = self.safe_input(prompt)
                value = float(value_str)
                if value < 0 or (not allow_zero and value == 0):
                    print("Only positive numbers allowed for input.")
                else:
                    return value
            except ValueError:
                print("Your input is not a number. Please enter a numeric value.")

    def main_menu(self):
        while True:
            print("Welcome to your personal budgeting app. \n 1. Add to one of your expense categories \n 2. View Summary \n 3. Set Savings Goal \n 4. View Remaining Balance \n 5. Exit")

            choice = self.safe_input("Select an option (1-5): ").strip()
            print()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_summary()
            elif choice == "3":
                self.set_savings_goal()
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                print("Thank you for using the Personal Budgeting App!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.\n")


def main():
    app = BudgetApp()
    print("Welcome to the Personal Budgeting Application!\n")
    app.set_user_income()
    app.main_menu()


if __name__ == "__main__":
    main()
    
    