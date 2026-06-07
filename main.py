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
            print(f"Account created successfully! \nUsername : {name} \nAccount Number: {acc_id}")

    #module to search account
    def search_account(self, acc_id):
        acc_id = input("Enter Account Number : ")

        for acc_id in accounts:
            if acc_id == accounts:
                print(f"Account found ! \nUsername : {self.accounts[acc_id]} \nAccount Number : {acc_id}")
            else:
                print("Account not found !!")
    

            