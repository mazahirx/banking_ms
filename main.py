import random
import string
class Bank:
    accounts = {}

    #constructor
    def __init__(self):
        pass

    #module to create account
    def create_account(self):
        name = input("Enter name : ")
        characters = string.digits
        #generate random acc_id of 11 numbers
        acc_id = "".join(random.choice(characters) for _ in range(11)) 

        self.accounts[acc_id] = name
        print(f"Account created successfully! \nUsername : {name} \nAccount Number: {acc_id}")

    #module to search account
    def search_account(self):
        acc_id = input("Enter Account Number : ")

        if acc_id in self.accounts:
            print(f"Account found ! \nUsername : {self.accounts[acc_id]} \nAccount Number : {acc_id}")
        else:
            print("Account not found !!")
        
    #module to delete account
    def delete_account(self):
        acc_id = input("Enter Account Number : ")

        if acc_id in self.accounts:
            del self.accounts[acc_id]
            print("Account Deleted !")
        else:
            print("Account not found !!")
    
    
def main():

    b = Bank()

    print("---- BANKING ACCOUNTS ----")
    


    while True:
        print("\n---- Welcome to the menu ----")
        print("1.Create Account \n2.Search Account \n3.Delete Account \n4.Exit")

        choice = int(input("Chose Option : "))
        
        if choice == 1:
            b.create_account()
        elif choice == 2:
            b.search_account()
        elif choice == 3:
            b.delete_account()
        elif choice == 4:
            print("Exiting....")
            break
        else:
            print("Choose valid option!")

if __name__ == "__main__":
    main()