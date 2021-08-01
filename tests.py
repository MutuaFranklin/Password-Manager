import unittest
from unittest.case import TestCase
from appClasses import Credentials, User
import pyperclip


class TestUser(unittest.TestCase):

    """
    Test class defines test cases for the User Class behaviors
    """

    def setUp(self):

        """
        Set up method to run before each test cases
        """
        self.newUser = User("Franklin", "Mutua", "Frankfreek", "ankeek80")


    def tearDown(self):
        """
        tearDown method that does clean up after each test case has been return
        """
        User.usersList=[]

    def test_init(self):
    
        """
        test_init case to test if the object is initialized properly
        """

        self.assertEqual(self.newUser.firstname, "Franklin")
        self.assertEqual(self.newUser.lastname, "Mutua")
        self.assertEqual(self.newUser.username, "Frankfreek")
        self.assertEqual(self.newUser.password, "ankeek80")

    def test_save_new_user(self):
        self.newUser.save_new_user()
        self.assertEqual(len(User.usersList),1)


    def test_save_multiple_users(self):
        """
        test case to test if we can save multiple users in the usersList
        """
        self.newUser.save_new_user()
        testUser = User("TestFlorence", "TestNjeri", "TestFlonjeri", "TestFlon203")
        testUser.save_new_user()
        self.assertEqual(len(User.usersList),2)

    def test_delete_user(self):
        """
        test case to test if we can remove a user from the usersList
        """
        self.newUser.save_new_user()
        testUser = User("TestFlorence", "TestNjeri", "TestFlonjeri", "TestFlon203")
        testUser.save_new_user()
        self.newUser.delete_user()
        self.assertEqual(len(User.usersList),1)

    

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the contact
        """
        self.newUser.save_new_user()
        testuser=User("firstname", "lastname", "username", "password")
        testuser.save_new_user()

        if_user_exists= User.if_user_exists("username")
        self.assertTrue(if_user_exists)


  
class TestCredentials(unittest.TestCase):
    """
    Test class defines test cases for the Credentials Class behaviors
    """
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.newAccount = Credentials("Instagram", "Widget", "12345")


    def tearDown(self):
        """
        tearDown method that does clean up after each test case has been return
        """
        Credentials.userAccounts=[]

    
    def test_init(self):
        """
        test case to test if the object is initialized properly
        """
        self.assertEqual(self.newAccount.siteName,"Instagram")
        self.assertEqual(self.newAccount.accountUsername, "Widget")
        self.assertEqual(self.newAccount.accountPassword, "12345")


    def test_save_account(self):
        """
        test case to test if the credentials object is saved into userAccounts
        """

        self.newAccount.save_new_userAccount()
        self.assertEqual(len(Credentials.userAccounts),1)


    def test_save_multiple_accounts(self):
        """
        test case to test if we can save multiple credentials to userAccounts
        """

        self.newAccount.save_new_userAccount()
        testaccount = Credentials("Instagram", "Widget", "12345" )
        testaccount.save_new_userAccount()
        self.assertEqual(len(Credentials.userAccounts),2)

     

    
    def test_delete_account(self):
        """
        test case to test if we can remove a credential from our userAccount
        """
        self.newAccount.save_new_userAccount()
        testaccount = Credentials("Instagram", "Widget", "12345")
        testaccount.save_new_userAccount()
        self.newAccount.delete_user_account()
        self.assertEqual(len(Credentials.userAccounts),1)


    def test_account_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the contact.
            '''

            self.newAccount.save_new_userAccount()
            test_contact = Credentials("Instagram", "Widget", "12345") 
            test_contact.save_new_userAccount()
            account_exists = Credentials.account_exist("Instagram")

            self.assertTrue(account_exists)




    def test_display_all_accounts(self):
        """
        test case to test if a list of all users saved can be returned        
        """
        self.assertEqual(Credentials.display_accounts(), Credentials.userAccounts)

    



    def test_find_siteName(self):
        """
        test to check if we can find  and display an account credential using site name 
        """
        self.newAccount.save_new_userAccount()
        testaccount = Credentials("Instagram", "Widget", "12345")
        testaccount.save_new_userAccount()

        foundaccount = Credentials.find_by_siteName("Instagram")
        self.assertEqual(foundaccount.siteName, testaccount.siteName)


    # def test_copy_accountUsername(self):
    #     '''
    #     Test to confirm that we are copying the account username from a found credentials
    #     '''

    #     self.newAccount.save_new_userAccount()
    #     Credentials.copy_accountUsername("Widget")
    #     self.assertEqual(self.newAccount.accountUsername, pyperclip.paste())


    # def test_copy_accountPassword(self):
    #     '''
    #     Test to confirm that we are copying the account password from a found credentials
    #     '''

    #     self.newAccount.save_new_userAccount()
    #     Credentials.copy_accountPassword("Facebook")
    #     self.assertEqual(self.newAccount.accountPassword, pyperclip.paste())







    


if __name__ == '__main__':
    (unittest.main())
