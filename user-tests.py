import unittest
from unittest.case import TestCase
from user import Credentials, User
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

    def test_display_all_users(self):
        """
        test case to test if a list of all users saved can be returned
        """
        self.assertEqual(User.display_users(), User.usersList)

        

    def test_find_user_by_username(self):
        """
        test case to check if we can find a user by their password and display the user
        """

        self.newUser.save_new_user()
        testuser=User("TestFlorence", "TestNjeri", "TestFlonjeri", "TestFlon203")
        testuser.save_new_user()

        found_user = User.find_by_username("TestFlonjeri")
        self.assertEqual(found_user.username,testuser.username)


    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the contact
        """
        self.newUser.save_new_user()
        testuser=User("TestFlorence", "TestNjeri", "TestFlonjeri", "TestFlon203")
        testuser.save_new_user()

        if_user_exists= User.if_user_exists("TestFlonjeri")
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
        Credentials.userAccounts[]









    


if __name__ == '__main__':
    (unittest.main())
