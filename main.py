

import bank_operation as operation
def main():
    print("---------------------------- Welcome to our banking app -------------------------")
    while True:
        print("\n")
        print("Options: ")
        print("1. create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance ")
        print("5. Delete account ")
        print("6. Exit")
        try:
            user_choice = int(input("Enter your choice: "))
            assert 1<= user_choice <=6,"option not availble"

            if user_choice == 1:
                print("---------------- Create Account --------------")
                name = input("Enter your name: ")
                initial_balance = int(input("Enter your initial balance: "))
                password = input("Create your password: ")
                operation.create_account(name,initial_balance,password)


            elif user_choice == 2:
                print("---------------- Deposite  --------------")
                name = input("Enter your name: ")
                deposit_amount = int(input("Enter the desposite amount: "))
                operation.deposite(name,deposit_amount)


            elif user_choice == 3:
                print("---------------- Withdraw  --------------")
                name = input("Enter your name: ")
                withdraw_amount = int(input("Enter the withdraw amount: "))
                password = input("Enter your password: ")
                operation.withdraw(name,withdraw_amount,password)


            elif user_choice == 4:
                print("---------------- Check Balance --------------")
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                operation.check_balance(name,password)



            elif user_choice == 5:
                print("---------------- Delete Account --------------")
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                operation.delete_account(name,password)


            elif user_choice == 6:
                print("Thank you for using our service")
                print("exiting...")
                break
        except ValueError:
            print("Choose correct option ")
        except AssertionError as error:
            print(error)

            
if __name__=="__main__":
    main()        

