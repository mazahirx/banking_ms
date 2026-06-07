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
                print(f"Balance : {self.accounts[self.balance]}")
            else:
                print("Account not found !!")

    #module to delete account
    def delete_account(self):
        self.acc_id = input("Enter Account Number : ")

        for self.acc_id in self.accounts:
            if self.acc_id == self.accounts:
                self.accounts[self.acc_id] = ""
                print("Account Deleted !")
            else:
                print("Account not found !!")
    
    #module to add balance
    def add_balance(self):
        self.acc_id = input("Enter Account Number : ")
        self.balance = input("Enter the amount : ")

        for self.acc_id in self.accounts:
            self.accounts[self.acc_id] = [self.balance]
            print("Balance added successfully")
    