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
    def create_account(self):
        self.name = input("Enter name : ")
        characters = string.digits
        #generate random acc_id of 11 numbers
        self.acc_id = "".join(random.choice(characters) for _ in range(11)) 

        self.accounts[self.acc_id] = self.name
        print(f"Account created successfully! \nUsername : {self.name} \nAccount Number: {self.acc_id}")

    #module to search account
    def search_account(self):
        self.acc_id = input("Enter Account Number : ")

        if self.acc_id in self.accounts:
            print(f"Account found ! \nUsername : {self.accounts[self.acc_id]} \nAccount Number : {self.acc_id}")
        else:
            print("Account not found !!")
        
    #module to delete account
    def delete_account(self):
        self.acc_id = input("Enter Account Number : ")

        #for self.acc_id in self.accounts:
        if self.acc_id in self.accounts:
            del self.accounts[self.acc_id]
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
    
def main():

    a1 = Account("Test",25,0)

    print("---- BANKING ACCOUNTS ----")
    


    while True:
        print("\n---- Welcome to the menu ----")
        print("1.Create Account \n2.Search Account \n3.Delete Account \n4.Add Balance \n5.Exit")

        choice = int(input("Chose Option : "))
        
        if choice == 1:
            a1.create_account()
        elif choice == 2:
            a1.search_account()
        elif choice == 3:
            a1.delete_account()
        elif choice == 4:
            a1.add_balance()
        elif choice == 5:
            print("Exiting....")
            break
        else:
            print("Choose valid option!")

if __name__ == "__main__":
    main()