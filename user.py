import pyperclip
import random


class User:
    """
    Class that generates new instances of users.
    """

    usersList=[]
    
    def __init__(self, firstname, lastname, username, password):
        """
        __init__ method defines properties for our objects self.

        Args:
        firstname: New user first name
        lastname: New user last name
        username: New user username
        password: New user password

        """

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password =password

    def save_new_user(self):

        """
        method saves new user objects into user userslist array
        """

        User.usersList.append(self)


    def delete_user(self):
        """
        method deletes user from the userslist 
        """
        User.usersList.remove(self)

    @classmethod
    def display_users(cls):
        """
        method returns User userslist
        """

        return cls.usersList


    #A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.
    @classmethod
    def find_by_number(cls,number):
        """
        Method that takes in a password as number and returns a user that matches that number

        Args:
        number: password to search for Returns: user if that  password matches.
        """
        for user in cls.usersList:
            if user.password == number:
                return user


    @classmethod
    def find_by_username(cls,text):
        """
        Method that takes in a username as text and returns a user that matches that username

        Args:
        text: username to search for users and Returns: user if that  username matches.
        """
        for user in cls.usersList:
            if user.username == text:
                return user

   

   
    @classmethod
    def if_user_exists(cls, number):
        '''
        Method that checks if a user exists from the usersList.
        Args:
            text: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.usersList:
            if user.username == number:
                return True
                return False


class Credentials:
    """
    Class that generates new instances of Credentials
    """
    userAccounts = []


    def __init__(self, siteName, accountUsername, accountPassword):
        """
        __init__ method defines properties for our objects self.

        Args:
        accountName: New Credentials accountName
        accountUsername: New Credentials accountUsername
        accountPassword: New Credentials accountPassword
        """
        self.siteName = siteName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    def save_new_userAccount(self):
        """
        method saves new user credentials objects into user userAccounts array
        """
        Credentials.userAccounts.append(self)


    def delete_user_account(self):
        """
        method delete account credentials from the userAccounts
        """
        Credentials.userAccounts.remove(self)

    
    @classmethod
    def display_accounts(cls):
        """
        method returns User userslist
        """
        return cls.userAccounts

  
    @classmethod
    def find_by_siteName(cls, text):
        """
        Method that takes in a number and returns a contact that matches that number

        Args:
        number: accountusername to search for Returns: Credentials of user that matches the number.
        """
        for userAccounts in cls.userAccounts:
            if userAccounts.siteName == text:
                return userAccounts

    @classmethod
    def account_exist(cls,text):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.userAccounts:
            if account.siteName == text:
                    return True

        return False



    @classmethod
    def copy_accountUsername(cls,text):
        '''
        Test to confirm that we are copying the account username from a found account credentials
        '''
        foundaccount = Credentials.find_by_siteName(text)
        pyperclip.copy(foundaccount.accountUsername)


    @classmethod
    def copy_accountPassword(cls,text):
        '''
        Test to confirm that we are copying the account password from a found account credentials
        '''
        foundaccount = Credentials.find_by_siteName(text)
        pyperclip.copy(foundaccount.accountPassword)


    







    



