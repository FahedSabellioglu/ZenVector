import unittest
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ZenVector.views import *


class TestUrls(SimpleTestCase):

    def test_page_home(self):
        url = reverse("PutTogether")
        called_func = resolve(url).func
        self.assertEqual(called_func,page_Home)

    def test_Signup(self):
        called_func = resolve("/PutTogether/Signup/").func
        self.assertEqual(called_func,Signup)

    def test_Login(self):
        called_func = resolve("/PutTogether/Login/").func
        self.assertEqual(called_func,Login)

    def test_Plans(self):
        called_func = resolve('/PutTogether/PlanBuy/').func
        self.assertEqual(called_func,Signup)

    def test_Logout(self):
        called_func = resolve("/PutTogether/Loguout/").func
        self.assertEqual(called_func,Logout)

    def test_LoggedPassChange(self):
        called_func = resolve("/PutTogether/PasswordChange/").func
        self.assertEqual(called_func,Logged_change_password)






if __name__ == '__main__':
    unittest.main()
