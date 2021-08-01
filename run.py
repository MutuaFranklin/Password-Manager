#!/usr/bin/env python3.8
from appClasses import User
from appClasses import Credentials
import pyperclip
import string
import random


def create_user(firstname, lastname, username, password):
    newUser= User(firstname,lastname, username, password)

    return newUser


def save_new_user(user):
    user.save_new_user()


def delete_user(user):
    user.delete_user()


def display_users():
    return User.display_users()


def find_user(number):
    return User.find_by_number(number)



def create_account(siteName, accountUsername, accountPassword):
    newAccount= Credentials(siteName, accountUsername, accountPassword)
    return newAccount


def save_new_userAccount(user):
    user.save_new_userAccount()


def delete_user_account(user):
    user.delete_user_account()


def check_existing_accounts(text):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.account_exist(text)



def display_accounts():
    return Credentials.display_accounts()
    

def find_account(number):
    return Credentials.find_by_number(number)


def find_account(text):
    return Credentials.find_by_siteName(text)




def main():

    User.usersList =[]
    Credentials.userAccounts =[]


    while True:

        print(""*10)
        print("Hello, Welcome to password manager. If a registered user, Select Login otherwise SignUp")
        print("-"*87)
        print("Use l for LogIn or s for SignUp")
        print(""*10)

        selection = input()
        print(""*10)

        if selection == "SignUp" or selection == "s":
            print("Create a user account")
            print("-"*21)

            print("Enter your First Name: ")
            firstname=input().lower()
            print(""*10)

            print("Enter your Last Name: ")
            lastname=input().lower()
            print(""*10)

            print("Set your username: ")
            username=input().lower()
            print(""*10)

            print("Set your account password: ")
            password=input().lower()
            print(""*10)


            save_new_user(create_user(firstname, lastname, username, password))


            print(f"Thank you {username} for registering an account with us. Now you can login")
            print("\n")

        elif selection == "LogIn" or selection == "l":

            while True:
                print("Login to your user account")
                print("-"*30)

                print("Enter your Username: ")
                loginUsername=input().lower()
                print(""*10)

                print("Enter your password: ")
                loginPassword=input().lower()

                for user in User.usersList:
                    if ((user.username == loginUsername) and (user.password == loginPassword)):
                        
                        print("\n")

                        while True:

                            print(f"{user.username} Welcome to Password Manager App. Keep your Password secure")
                            print("-"*64)
                            print("Use these key terms to navigate the app:-")
                            print(""*10)
                            print(" ac - add a new account credentials")
                            print(" vc - display all user accounts")
                            print(" sc - search account credentials")
                            print(" dc - delete selected account credentials")
                            print(" ex - exit the app")
                            print(""*10)

                            navigate = input().lower()
                            print("\n")
                            
                            if navigate == "ac":
                                print("Enter user account credentials")
                                print("-"*30)
                                print("Enter the site or app name")
                                siteName = input().lower()
                                print(""*10)

                                print("Enter accounts username")
                                accountUsername = input().lower()
                                print(""*10)

                                print("Enter gp- to automatically generate a password or cp- to create your own custom password")
                                print("-"*90)

                                choice = input().lower()
                                print(""*10)


                                if choice == "gp":
                                    # passCharacters=string.ascii_letters + string.hexdigits
                                    # accountPassword="".join(choice(passCharacters)for x in range(randint(8,16)))
                                    characters = string.ascii_letters + string.digits + string.punctuation
                                    accountPassword = ''.join(random.choice(characters) for i in range(16))
                                    print(f"Your generated {siteName} password is: {accountPassword}")

                                elif choice=="cp":
                                            print(f"Enter your {siteName} Password")
                                            accountPassword=input().lower()

                                else:
                                    print("Invalid Choice,try again")

                                save_new_userAccount(create_account(siteName, accountUsername, accountPassword))
                                print("\n")
                                print(f" Site/app name:{siteName} \n Account Name: {accountUsername} \n Password set: {accountPassword}")
                                print('\n')

                            elif navigate == "vc":
                                if len(Credentials.userAccounts) >= 1:
                                    if find_account(siteName):
                                        print("Here is the list of all your accounts: ")
                                        print("-"*39)
                    

                                        for account in display_accounts():
                                            print(f" Site Name: {account.siteName} \n Account Username: {account.accountUsername} \n Password: {account.accountPassword} \n")
                                            print('\n')
                                    else:
                                        print("Account does not exits")
                                else:
                                    print('\n')
                                    print("Here is the list of all your accounts: ")
                                    print('\n')
                                    print("   You don't seem to have any account credentials saved yet!!")
                                    print('\n')

                            elif navigate == 'sc':
                                if len(Credentials.userAccounts) >= 1:
                
                                    print("Enter the site name of the account credentials you want to search")
                                    searchInput = input().lower()
                                    if check_existing_accounts(searchInput):
                                            print(""*10)
                                            search_account = find_account(searchInput)
                                            print(""*10)
                                            print(f"Site Name: {search_account.siteName}")
                                            print('-' * 30)

                                            print(f"Account Username.....{search_account.accountUsername}")
                                            print(f"Account Password......{search_account.accountPassword}")
                                            print('\n')
                                    else:
                                        print("That account does not exist")

                                else:
                                    print('\n')
                                    print("   You don't seem to have any account credentials saved yet!!")
                                    print('\n')


                            elif navigate == "dc":
                                if len(Credentials.userAccounts) >= 1:
                                    if find_account(siteName):
                                        print("Here is the list of all your accounts: ")
                                        print("-"*39)
                    

                                        for account in display_accounts():
                                            print(f" Site Name: {account.siteName} \n Account Username: {account.accountUsername} \n Password: {account.accountPassword} \n")
                                            print('\n')

                                        print("Enter the site name of the account credentials you want to delete")
                                        print("-"*60)
                                        delInput = input().lower()

                                        print('\n')

                                        if check_existing_accounts(delInput):
                                                print(""*10)
                                                del_account = find_account(delInput)
                                                print(""*10)
                                                print(f"Are you sure you want to delete the account with the following credentials: Yes or No")
                                                print(""*10)

                                                print(f"Account Site Name.....{del_account.siteName}")
                                                print(f"Account Username.....{del_account.accountUsername}")
                                                print(f"Account Password......{del_account.accountPassword}")
                                                print('\n')

                                                delete = input().lower()
                                                print('\n')

                                                if delete == "yes":
                                                    delete_user_account(del_account)
                                                

                                                    print(f"Your account credentials has been successfully deleted")
                                                    print("Your new list of accounts includes: ")
                                                    print("--"*20)
                                                    for accountList in Credentials.userAccounts:
                                                        print(f"Site Name: {accountList.siteName}")
                                                        print(f"Account Name: {accountList.accountUsername}")
                                                        print(f"Account Password: {accountList.accountPassword}")
                                                        print('\n')

                                                elif delete == "no":
                                                    print("Okay, Navigate to other options below....")
                                                    print('\n')
                                        else:
                                            print("The account requested does not seem to exist")
                                        
                                else:                                      
                                    print('\n')
                                    print("You don't seem to have any account credentials saved yet")
                                    print('\n')
                            


                            elif navigate == "ex":
                                print("Bye .......")
                                print('\n')
                                break
                                
                    

                            else:                    
                                print("Invalid option, please try again")
                                print("\n")
                                
                        
                    break

                else:
                    print("Incorrect username or password, please try again")
                    print("\n")
                         
                
        
        else:
            print("Incorrect option,choose from the one's listed")
            print("\n")
            
        






if __name__ == '__main__':
    main()