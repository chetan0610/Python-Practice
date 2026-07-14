"""
Mini Project 3: Banking System
Description: A menu-driven banking application handling deposits, withdrawals, and history.
Prevents overdrafts and validates input.
"""

def initialize_account(account_holder, initial_balance=0.0):
    """Creates a dictionary representing a bank account."""
    return {
        "name": account_holder,
        "balance": initial_balance,
        "history": [f"Account created with ${initial_balance:.2f}"]
    }

def deposit_funds(account, amount):
    """Adds funds to the account and logs the transaction."""
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return
    
    account["balance"] += amount
    transaction = f"Deposited: ${amount:.2f}"
    account["history"].append(transaction)
    print("Deposit successful.")

def withdraw_funds(account, amount):
    """Removes funds if available, preventing overdraft."""
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return
        
    if amount > account["balance"]:
        print(f"Transaction Denied: Insufficient funds. Current balance: ${account['balance']:.2f}")
        return
        
    account["balance"] -= amount
    transaction = f"Withdrew: ${amount:.2f}"
    account["history"].append(transaction)
    print("Withdrawal successful.")

def check_balance(account):
    """Displays the current account balance."""
    print(f"Current Balance for {account['name']}: ${account['balance']:.2f}")

def show_transaction_history(account):
    """Prints all historical transactions for the account."""
    print("\n--- Transaction History ---")
    for record in account["history"]:
        print(f"- {record}")
    print("---------------------------")

if __name__ == "__main__":
    print("Welcome to Python Bank")
    user_name = input("Enter account holder name: ").strip()
    my_account = initialize_account(user_name)
    
    while True:
        print("\nMain Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '5':
            print("Thank you for using Python Bank. Goodbye!")
            break
            
        if choice in ('1', '2'):
            try:
                transaction_amount = float(input("Enter amount: $"))
                if choice == '1':
                    deposit_funds(my_account, transaction_amount)
                else:
                    withdraw_funds(my_account, transaction_amount)
            except ValueError:
                print("Invalid input. Please enter a valid currency amount.")
        elif choice == '3':
            check_balance(my_account)
        elif choice == '4':
            show_transaction_history(my_account)
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")