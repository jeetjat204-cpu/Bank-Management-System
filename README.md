# Bank Management System

## Overview

Bank Management System is a Python-based banking simulation developed as an academic project. It simulates basic banking operations through a simple command-line interface.

The project demonstrates the use of Python programming concepts such as functions, dictionaries, conditional statements, loops, input validation, and random number generation.

> **Note:** This project is an academic simulation and does not connect to or perform transactions with a real bank.

## Features

* Create a new bank account
* Generate a unique account number
* Select Savings or Current account type
* Set and confirm a 4-digit PIN
* Login using account number and PIN
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* Generate transaction IDs
* View transaction history
* View account details
* Change account PIN
* Logout from the account
* Input validation for important fields

## Functional Modules

### 1. Account Management

The system allows users to create accounts, log in, view account details, and change their PIN.

### 2. Banking Transactions

Users can deposit money, withdraw money, and transfer money to another account.

### 3. Account Information

Users can check their current balance and view their transaction history.

## Technologies Used

* Python 3
* Python Standard Library
* `random` module
* Command-Line Interface (CLI)

## Requirements

* Python 3.x
* A computer with a command-line/terminal environment

No external Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python bank_management.py
```

If your system uses `python3`, use:

```bash
python3 bank_management.py
```

## How to Use

After starting the program, the main menu provides the following options:

1. Create New Account
2. Login
3. Bank Information
4. Exit

After logging in, users can access:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Transaction History
6. Account Details
7. Change PIN
8. Logout

## Input Validation

The program validates several user inputs, including:

* Empty account names
* 10-digit mobile numbers
* 4-digit PINs
* PIN confirmation
* Minimum initial deposit
* Positive transaction amounts
* Existing receiver account numbers
* Sufficient account balance
* Correct PIN during authentication and transfers

## Testing

The project can be tested by running the program and checking the following operations:

* Creating a new account
* Logging in with correct and incorrect credentials
* Checking account balance
* Depositing money
* Withdrawing money
* Attempting a withdrawal with insufficient balance
* Transferring money between accounts
* Viewing transaction history
* Viewing account details
* Changing the PIN
* Logging out

## Project Structure

```text
Bank-Management-System/
│
└── bank_management.py
```

## Academic Purpose

This project was developed as part of the VITyarthi Build Your Own Project activity. It demonstrates the practical application of Python programming concepts in a banking simulation.

## Disclaimer

This is an educational software project. It is not connected to any real banking institution and should not be used for actual financial transactions.
