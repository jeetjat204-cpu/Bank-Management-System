import random
# -----------------------------------------
# BANK MANAGEMENT SYSTEM
# -----------------------------------------
acc = {}
def acc_number():
    while True:
        number = str(random.randint(10000000, 99999999))
        if number not in acc:
            return number

def transaction_id():
    return "TXN" + str(random.randint(100000, 999999))

def valid(value):
    return value.isdigit()

def create_acc():
    print("\n" + "=" * 45)
    print("           CREATE NEW ACCOUNT")
    print("=" * 45)
    name = input("Enter your full name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    mobile = input("Enter mobile number: ")
    if not valid(mobile) or len(mobile) != 10:
        print("Please enter a valid 10-digit mobile number.")
        return
    print("\nAccount Type")
    print("1. Savings")
    print("2. Current")
    account_choice = input("Choose account type: ")
    if account_choice == "1":
        account_type = "Savings"
    elif account_choice == "2":
        account_type = "Current"
    else:
        print("Invalid account type.")
        return
    pin = input("Create a 4-digit PIN: ")
    if not valid(pin) or len(pin) != 4:
        print("PIN must contain exactly 4 digits.")
        return
    confirm_pin = input("Confirm PIN: ")
    if pin != confirm_pin:
        print("PINs do not match.")
        return
    initial_deposit = input("Enter initial deposit: ")
    if not valid(initial_deposit):
        print("Please enter a valid amount.")
        return
    initial_deposit = int(initial_deposit)
    if initial_deposit < 500:
        print("Minimum initial deposit is Rs. 500.")
        return
    account_number = acc_number()
    acc[account_number] = {"name": name,"mobile": mobile,"type": account_type,"pin": pin,"balance": initial_deposit,"transactions": ["Account opened with Rs. " + str(initial_deposit)]}
    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Account Type:", account_type)
    print("Initial Balance: Rs.", initial_deposit)

def login():
    print("\n" + "=" * 45)
    print("                 LOGIN")
    print("=" * 45)
    account_number = input("Enter account number: ")
    if account_number not in acc:
        print("Account not found.")
        return
    pin = input("Enter PIN: ")
    if acc[account_number]["pin"] != pin:
        print("Incorrect PIN.")
        return
    print("\nLogin successful!")
    print("Welcome,", acc[account_number]["name"])
    account_menu(account_number)

def check_balance(account_number):
    balance = acc[account_number]["balance"]
    print("\n-----------------------------")
    print("       ACCOUNT BALANCE")
    print("-----------------------------")
    print("Available Balance: Rs.", balance)

def deposit(account_number):
    print("\n" + "=" * 45)
    print("              DEPOSIT")
    print("=" * 45)
    amount = input("Enter amount to deposit: ")
    if not valid(amount):
        print("Invalid amount.")
        return
    amount = int(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    acc[account_number]["balance"] += amount
    txn_id = transaction_id()
    acc[account_number]["transactions"].append(txn_id + " - Deposited Rs. " + str(amount))
    print("\nDeposit successful!")
    print("Amount Deposited: Rs.", amount)
    print("New Balance: Rs.", acc[account_number]["balance"])

def withdraw(account_number):
    print("\n" + "=" * 45)
    print("             WITHDRAW")
    print("=" * 45)
    amount = input("Enter amount to withdraw: ")
    if not valid(amount):
        print("Invalid amount.")
        return
    amount = int(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    balance = acc[account_number]["balance"]
    if amount > balance:
        print("Insufficient balance.")
        return
    acc[account_number]["balance"] -= amount
    txn_id = transaction_id()
    acc[account_number]["transactions"].append(txn_id + " - Withdrawn Rs. " + str(amount))
    print("\nWithdrawal successful!")
    print("Amount Withdrawn: Rs.", amount)
    print("Remaining Balance: Rs.", acc[account_number]["balance"])

def transfer(account_number):
    print("\n" + "=" * 45)
    print("             MONEY TRANSFER")
    print("=" * 45)
    receiver = input("Enter receiver account number: ")
    if receiver not in acc:
        print("Receiver account not found.")
        return
    if receiver == account_number:
        print("You cannot transfer money to your own account.")
        return
    amount = input("Enter amount to transfer: ")
    if not valid(amount):
        print("Invalid amount.")
        return
    amount = int(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if amount > acc[account_number]["balance"]:
        print("Insufficient balance.")
        return
    pin = input("Enter your PIN to confirm: ")
    if pin != acc[account_number]["pin"]:
        print("Incorrect PIN. Transfer cancelled.")
        return
    acc[account_number]["balance"] -= amount
    acc[receiver]["balance"] += amount
    txn_id = transaction_id()
    acc[account_number]["transactions"].append(txn_id + " - Sent Rs. " + str(amount) +" to " + receiver)
    acc[receiver]["transactions"].append(txn_id + " - Received Rs. " + str(amount) +" from " + account_number)
    print("\nTransfer successful!")
    print("Transaction ID:", txn_id)
    print("Amount Sent: Rs.", amount)
    print("Receiver:", acc[receiver]["name"])
    print("Remaining Balance: Rs.", acc[account_number]["balance"])

def transaction_history(account_number):
    print("\n" + "=" * 45)
    print("          TRANSACTION HISTORY")
    print("=" * 45)
    history = acc[account_number]["transactions"]
    if len(history) == 0:
        print("No transactions available.")
        return
    for i in range(len(history)):
        print(str(i + 1) + ".", history[i])

def account_details(account_number):
    account = acc[account_number]
    print("\n" + "=" * 45)
    print("             ACCOUNT DETAILS")
    print("=" * 45)
    print("Name          :", account["name"])
    print("Mobile        :", account["mobile"])
    print("Account No.   :", account_number)
    print("Account Type  :", account["type"])
    print("Balance       : Rs.", account["balance"])

def change_pin(account_number):
    print("\n" + "=" * 45)
    print("              CHANGE PIN")
    print("=" * 45)
    old_pin = input("Enter current PIN: ")
    if old_pin != acc[account_number]["pin"]:
        print("Incorrect current PIN.")
        return
    new_pin = input("Enter new 4-digit PIN: ")
    if not valid(new_pin) or len(new_pin) != 4:
        print("PIN must contain exactly 4 digits.")
        return
    confirm_pin = input("Confirm new PIN: ")
    if new_pin != confirm_pin:
        print("PINs do not match.")
        return
    acc[account_number]["pin"] = new_pin
    acc[account_number]["transactions"].append("PIN changed successfully")
    print("PIN changed successfully!")

def account_menu(account_number):
    while True:
        print("\n")
        print("=" * 45)
        print("          PYBANK ACCOUNT MENU")
        print("=" * 45)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Account Details")
        print("7. Change PIN")
        print("8. Logout")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            deposit(account_number)
        elif choice == "3":
            withdraw(account_number)
        elif choice == "4":
            transfer(account_number)
        elif choice == "5":
            transaction_history(account_number)
        elif choice == "6":
            account_details(account_number)
        elif choice == "7":
            change_pin(account_number)
        elif choice == "8":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n")
        print("=" * 50)
        print("              WELCOME TO PYBANK")
        print("=" * 50)
        print("1. Create New Account")
        print("2. Login")
        print("3. Bank Information")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            create_acc()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\n" + "=" * 45)
            print("             ABOUT PYBANK")
            print("=" * 45)
            print("PyBank is a Python-based banking simulation.")
            print("It demonstrates basic banking operations")
            print("using Python programming concepts.")
            print("\nThis is an academic simulation and")
            print("does not connect to a real bank.")
        elif choice == "4":
            print("\nThank you for using PyBank!")
            print("Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main_menu()
