import random
import string
class Account:
    accounts = {}

    #constructor
    def __init__(self, name, acc_id, balance):
        self.name = name
        self.acc_id = acc_id
        self.balance = balance

    #module to create account
    def create_account(self, accounts):
        name = input("Enter name : ")
        characters = string.ascii_letters
        #generate random acc_id of 5 letters
        acc_id = "".join(random.choice(characters) for _ in range(5)) 

        for name in accounts:
            accounts[acc_id] = name
        
        print(f"Account created successfully! \nUsername : {name} \nAccount ID: {acc_id}")