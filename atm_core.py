#Importing required Libraries
import time

# Global Variables
ac_balance = 10000
ac_pin = 1234
accepted_cards = ["Card", "card", "CARD"]

# Creating necessary functions
def greet(name):
    print(f"Hello {name}!")
    time.sleep(1)


def accepted_cards(card):
    if card in accepted_cards:
        print("Card accepted")
    else:
        print("Invalid Card, Try Again")
        print("You just have to type 'Card'")
    time.sleep(1)

    return card in accepted_cards


#atm_core.py
user_name = input(str("Enter User name: "))
greet(user_name)
