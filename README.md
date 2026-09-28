# Bank Management System

## Overview

Bank Management System is a Python-based banking simulation developed as an academic project for the VITyarthi Build Your Own Project activity.

The project simulates basic banking operations through a simple Command-Line Interface (CLI). It demonstrates fundamental Python programming concepts such as functions, dictionaries, conditional statements, loops, input validation, and random number generation.

> **Note:** This is an academic banking simulation. It does not connect to a real bank or perform real financial transactions.

## Features

- Create a new bank account
- Generate a unique account number
- Select Savings or Current account type
- Set and confirm a 4-digit PIN
- Login using account number and PIN
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- Generate transaction IDs
- View transaction history
- View account details
- Change account PIN
- Logout from the account
- Input validation for important fields
- Bank information section
- Exit option

## Functional Modules

### 1. Account Management

Includes:
- Create New Account
- Login
- Account Details
- Change PIN

### 2. Banking Transactions

Includes:
- Check Balance
- Deposit Money
- Withdraw Money
- Transfer Money

### 3. Transaction and Account Information

Includes:
- Transaction History
- Account Balance
- Account Details
- Transaction IDs

## Technologies Used

- Python 3
- Python Standard Library
- `random` module
- Command-Line Interface (CLI)

No external Python packages are required.

## Python Concepts Used

- Variables
- Strings
- Lists
- Dictionaries
- Functions
- Conditional statements
- `while` loops
- `input()`
- `print()`
- Basic input validation
- Random number generation

## Requirements

- Python 3.x
- A computer with a command-line/terminal environment
- No external Python packages are required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python bank_management.py
```

If your system uses `python3`:

```bash
python3 bank_management.py
```

## How to Use

After starting the program, the main menu provides:

1. Create New Account
2. Login
3. Bank Information
4. Exit

After successful login, users can access:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Transaction History
6. Account Details
7. Change PIN
8. Logout

## Input Validation

The program validates:

- Empty account names
- 10-digit mobile numbers
- 4-digit PINs
- PIN confirmation
- Minimum initial deposit
- Positive transaction amounts
- Existing receiver account numbers
- Sufficient account balance
- Correct PIN during authentication
- Correct PIN during money transfers
- Valid account type selection

## Data Handling

The project uses an in-memory Python dictionary named `acc` to maintain account information while the program is running.

Each account contains:
- Name
- Mobile number
- Account type
- PIN
- Balance
- Transaction history

### Limitation

The project does not use file handling or a database. Account information is available only during the current program execution and is lost when the program is closed.

## Testing

The project was tested through manual execution of the program.

The following operations were tested:

- Creating a new account
- Logging in with correct and incorrect credentials
- Checking account balance
- Depositing money
- Withdrawing money
- Attempting withdrawal with insufficient balance
- Transferring money between accounts
- Viewing transaction history
- Viewing account details
- Changing the PIN
- Logging out
- Viewing bank information
- Exiting the program

The project report contains the test results and execution screenshots.

## Project Structure

```text
Bank-Management-System/
│
├── bank_management.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
├── Bank_Management_System_Project_Report_Final.pdf
│
└── docs/
    └── diagrams.md
```

### Main Files

- **`bank_management.py`** — Complete Python implementation.
- **`README.md`** — Project information and instructions.
- **`statement.md`** — Project statement, scope, target users and high-level features.
- **`requirements.txt`** — Project requirements.
- **`docs/diagrams.md`** — Project design diagrams.
- **`Bank_Management_System_Project_Report_Final.pdf`** — Complete academic project report.

## Screenshots

The project report contains screenshots demonstrating:

- Account creation
- Login
- Balance enquiry
- Deposit
- Withdrawal
- Money transfer
- Transaction history
- Account details
- PIN change
- Logout
- Bank information
- Exit

## Academic Purpose

This project was developed as part of the **VITyarthi Build Your Own Project** activity.

The purpose of the project is to demonstrate the practical application of fundamental Python programming concepts through a banking simulation.

## Limitations

- The system is an academic simulation.
- It does not perform real financial transactions.
- Account information is stored only while the program is running.
- No database or persistent storage is used.
- The application uses a command-line interface.
- It is not connected to real banking services.
- It is not intended for actual financial use.

## Future Enhancements

Possible future enhancements include:

- Persistent storage
- Database integration
- Graphical user interface
- Web-based interface
- Stronger authentication
- Improved security
- Persistent user accounts
- Administrative functions
- Printable account statements
- Exportable transaction reports

## Disclaimer

This project is developed only for educational purposes.

It is not connected to any real banking institution and should not be used for actual financial transactions.

