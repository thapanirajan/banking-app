
import json
accounts = {}

def load_account():
    global accounts
    try:
        with open("account.json","r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = {}


def save_accounts():
    with open("account.json","w") as file:
        json.dump(accounts,file,indent=4)


def create_account(name,initial_balance,password):
    accounts[name] ={
        "name" : name,
        "password":password,
        "balance": initial_balance,
        "points" :0
    }
    save_accounts()
    print("----------- Account created successfully ---------------")
    print("--------------------------------------------")



def deposite(name,deposit_amount):
    load_account()
    if name not in accounts:
        print(" ------------- Error ------------------ ")
        print("User doesnot exits ")
        print("----------------------------------------")
        return
    new_balance = accounts[name]["balance"] + deposit_amount
    accounts[name]["balance"] += deposit_amount
    print("-----------------Deposited successfully ---------------")
    print(f"New balance : {new_balance}")
    save_accounts()
    print("--------------------------------------------")

def withdraw(name,withdraw_amount,password):
    load_account()
    if name not in accounts:
        print(" ------------- Error ------------------ ")
        print("User doesnot exits ")
        print("----------------------------------------")
        return
    if password == accounts[name]["password"]:
        available_amount = accounts[name]["balance"]
        if available_amount<withdraw_amount:
            print("Insufficient balance")
            print("----------------------------------------")
        new_balance = available_amount - withdraw_amount
        accounts[name]["balance"] -= withdraw_amount
        print("-----------Withdraw successfull ----------")
        print(f"New balance : {new_balance}")
        print("----------------------------------------")
        save_accounts()
    else:
        print("----------- Password Incorrect ------------------")
        print("Incorrect Password, please try again")

def check_balance(name,password):
    load_account()
    if name not in accounts:
        print("User doesnot exits ")
        print("----------------------------------------")
        return
    if password == accounts[name]["password"]:
        balance = accounts[name]["balance"]
        print(f"Your balance is Rs{balance}")
        print("----------------------------------------")
    else:
        print("Incorrect Password, please try again")
        print("----------------------------------------")
    
def delete_account(name,password):
    load_account()
    if name not in accounts:
        print("User doesnot exits")
        print("----------------------------------------")
        return
    if password == accounts[name]["password"]:
        confirm = input("Delete account?(yes/no): ")
        if confirm.lower() == "yes":
            del accounts[name]
            save_accounts()
            print(f"Account name : {name} has been deleted successfully. ")
            return
        else:
            print("Account deletion canceled. ")
            return
    else:
        print("Incorrect password")
        return
