# Bank Management System – Design Diagrams

## 1. System Architecture Diagram

```text
                    USER
                      |
                      v
                MAIN MENU
                 /   |   \
                /    |    \
               v     v     v
        CREATE ACCOUNT LOGIN BANK INFO
                       |
                       v
                 ACCOUNT MENU
                       |
       +---------------+---------------+
       |       |       |       |       |
       v       v       v       v       v
    Balance Deposit Withdraw Transfer History
       |       |       |       |       |
       +-------+-------+-------+-------+
                       |
                       v
                 ACC DICTIONARY

##2. WORKFLOW


START
  |
  v
MAIN MENU
  |
  +----> Create Account
  |          |
  |          v
  |    Enter Account Details
  |          |
  |          v
  |    Validate Details
  |          |
  |          v
  |    Generate Account Number
  |          |
  |          v
  |    Store in acc Dictionary
  |          |
  |          v
  |       MAIN MENU
  |
  +----> Login
             |
             v
       Enter Account Number
          and PIN
             |
             v
       Credentials Correct?
          /          \
        No            Yes
        |              |
        v              v
    Main Menu     ACCOUNT MENU
                       |
              +--------+--------+
              |        |        |
              v        v        v
           Deposit  Withdraw  Transfer
              |        |        |
              +--------+--------+
                       |
                       v
                 Other Options
                       |
                       v
                    Logout
                       |
                       v
                  MAIN MENU

##3. USE CASE DIAGRAM
+----------------------+
                    |  BANK MANAGEMENT     |
                    |       SYSTEM         |
                    |                      |
USER ------------> | Create Account       |
USER ------------> | Login                 |
USER ------------> | Check Balance         |
USER ------------> | Deposit Money         |
USER ------------> | Withdraw Money        |
USER ------------> | Transfer Money        |
USER ------------> | Transaction History   |
USER ------------> | Account Details       |
USER ------------> | Change PIN            |
USER ------------> | Logout                |
USER ------------> | Bank Information      |
USER ------------> | Exit                  |
                    +----------------------+

##4. SEQUENCE DIAGRAM
USER              MAIN MENU          LOGIN          ACCOUNT MENU
 |                    |                |                 |
 |--- Select Login -->|                |                 |
 |                    |--- login() --->|                 |
 |                    |                |                 |
 |--- Enter Account Number + PIN ------>|                 |
 |                    |                |                 |
 |                    |        Check Account/PIN         |
 |                    |                |                 |
 |                    |<--- Login Successful -----------|
 |                    |                |                 |
 |------------------------ Open Account Menu ------------>|
 |                                                      |
 |---------------- Select Banking Operation ----------->|
 |                                                      |
 |<---------------- Display Result --------------------|

##5. MODULE DIAGRAM
                    main_menu()
                         |
              +----------+----------+
              |          |          |
              v          v          v
         create_acc()  login()  Bank Information
                           |
                           v
                    account_menu()
                           |
       +-------+-------+---+---+-------+-------+
       |       |       |       |       |       |
       v       v       v       v       v       v
   check_  deposit  withdraw transfer history details
   balance                                      |
                                                v
                                           change_pin()


##6. DATA DESIGN
acc
 |
 +-- Account Number
       |
       +-- name
       +-- mobile
       +-- type
       +-- pin
       +-- balance
       +-- transactions
              |
              +-- Account opened
              +-- Deposit
              +-- Withdrawal
              +-- Transfer

##7. OVERALL PROJECT FLOW
USER
  |
  v
MAIN MENU
  |
  +---- Account Management
  |
  +---- Authentication
             |
             v
       ACCOUNT MENU
             |
             v
    Banking Transactions
             |
             v
    Transaction History
             |
             v
       ACC DICTIONARY
