#Importing required Libraries
import time

# Global Variables
AC_BALANCE = 10000
AC_PIN = 1234
ACCEPTED_CARDS_LIST = ["Card", "card", "CARD"]

# Creating necessary functions
def greet():
    name = input("Enter your name: ")
    if isinstance(name, str):
        print(f"Hello {name}!")
        time.sleep(1)
        print("Welcome to Python ATM")
        time.sleep(1)
    else: 
        print("Invalid Response, try again")
        
def user_verification():
    greet()
    while True:
        if accepted_cards(input("Please insert your card: ")):
            break
        else:
            time.sleep(1)
    
    while True:
        if pin_check(int(input("Enter your pin: "))):
            time.sleep(1)
            main()
            break
        else:
            time.sleep(1)
            
def accepted_cards(card):
    global ACCEPTED_CARDS_LIST
    if card in ACCEPTED_CARDS_LIST:
        print("Card accepted")
        return True
    else:
        print("Invalid Card, Try Again")
        print("You just have to type 'Card'")
        return False

def pin_check(pin):
    global AC_PIN
    if pin == AC_PIN:
        print("Correct Pin")
        return True
    else:
        print("Incorrect Pin, Try Again")
        return False

def cash_withdraw():
    global AC_BALANCE
    try:
        amount = int(input("Enter Withdrawal Amount: "))
        if amount <= AC_BALANCE:
            time.sleep(1)
            print("Withrawing...")
            time.sleep(2)
            AC_BALANCE -= amount
            print(f"Your new balance: {AC_BALANCE}")
            time.sleep(1)
            if not another_transaction():
                exit_program()
        else:
            print("Insufficient Balance")
    except ValueError:
        print("Invalid Input. please enter a valid amount to continue")
            
def cash_deposit():
    global AC_BALANCE
    try:
        amount = int(input("Enter Deposit Amount: "))
        time.sleep(1)
        print("Depositing...")
        time.sleep(2)
        AC_BALANCE += amount
        print(f"Your new balance is: {AC_BALANCE}")
        time.sleep(1)
        if not another_transaction():
            exit_program()
    except ValueError:
        print("Invalid Input. please enter a valid amount to continue")
   
def check_balance():
    print("Checking...")
    print(f"Your balance is: {AC_BALANCE}")
    time.sleep(1)
    if not another_transaction():
        exit_program()

def another_transaction():
    main_screen_option = input("Would you like to make another transaction? (Y/N): ").lower()
    return main_screen_option == "y"
    
def main():
    while True:
        print("Here are your options:\n 1. Check Balance\n 2. Cash Withdrawal\n 3. Cash Deposit\n 4. Exit")
        user_option = input("Select appropriate option: ")

        if user_option == "1":
            time.sleep(1)
            check_balance()

        elif user_option == "2":
            time.sleep(1)
            cash_withdraw()

        elif user_option == "3":
            time.sleep(1)
            cash_deposit()

        elif user_option == "4":
            print("Thank you for using Python ATM")
            time.sleep(1)
            exit_program()

            break

        else:
            print("Invalid Input")

def exit_program():
    print("Thank you for using Python ATM")
    time.sleep(1)

    print("Exiting... .... Bye Bye!")
    time.sleep(1)
    exit()

# Start the ATM program
user_verification()
