#Importing required Libraries
import time

# Global Variables
ac_balance = 10000
ac_pin = 1234
accepted_cards_list = ["Card", "card", "CARD"]

# Creating necessary functions
def greet():
    name = input("Enter your name: ")
    if type(name) == str:
        print(f"Hello {name}!")
        time.sleep(1)
        print("Welcome to Python ATM")
        time.sleep(1)
    else: 
        print("Invalid Response, try again")

def user_verification():
    while True:
        greet()
        accepted_cards(card=input("Please insert your card: "))
        time.sleep(1)
        pin_check(pin=int(input("Enter your pin: ")))
        time.sleep(1)
        main()
        break

def accepted_cards(card):
    global accepted_cards_list
    if card in accepted_cards_list:
        print("Card accepted")
        return True
    else:
        print("Invalid Card, Try Again")
        print("You just have to type 'Card'")
        return False

def pin_check(pin):
    global ac_pin
    if pin == ac_pin:
        print("Correct Pin")
        return True
    else:
        print("Incorrect Pin, Try Again")
        return False

def cash_withdraw():
    global ac_balance
    amount = int(input("Enter Withdrawal Amount: "))
    if amount <= ac_balance:
        time.sleep(1)
        print("Withrawing...")
        time.sleep(2)
        ac_balance -= amount
        print(f"Your new balance: {ac_balance}")
        time.sleep(1)
        main_screen_option = input("Would you like to make another transaction? (Y/N): ")
        if main_screen_option.lower() == "y":
            main()
        else:
            exit_program()
    else:
        print("Insufficient Balance")

def cash_deposit():
    global ac_balance
    amount = int(input("Enter Deposit Amount: "))
    time.sleep(1)
    print("Depositing...")
    time.sleep(2)
    ac_balance += amount
    print(f"Your new balance is: {ac_balance}")
    time.sleep(1)
    main_screen_option = input("Would you like to make another transaction? (Y/N): ")
    if main_screen_option.lower() == "y":
        main()
    else:
        exit_program()
   
def check_balance():
    print("Checking...")
    print(f"Your balance is: {ac_balance}")
    time.sleep(1)
    main_screen_option = input("Would you like to make another transaction? (Y/N): ")
    if main_screen_option.lower() == "y":
        main()
    else:
        exit_program()
    
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

# Calling Functions
user_verification()
