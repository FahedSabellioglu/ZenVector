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

    def test_DeleteAccount(self):
        called_func = resolve("/PutTogether/DeleteAccount/").func
        self.assertEqual(called_func, DeleteAccount)

    def test_RequestPasswordResetCode(self):
        called_func = resolve("/PutTogether/forgotPass/").func
        self.assertEqual(called_func, RequestPasswordResetCode)

    def test_PasswordResetCodeValidity(self):
        called_func = resolve("/PutTogether/CheckCode/").func
        self.assertEqual(called_func, PasswordResetCodeValidity)

    def test_NonLogged_ResetPassword(self):
        called_func = resolve("/PutTogether/PasswordReset/").func
        self.assertEqual(called_func, NonLogged_ResetPassword)

    def test_CreateProject(self):
        called_func = resolve("/PutTogether/Projects/CreateProject/").func
        self.assertEqual(called_func, CreateProject)

    def test_DeleteProject(self):
        called_func = resolve("/PutTogether/Projects/DeleteProject/").func
        self.assertEqual(called_func, DeleteProject)

    def test_ChangeProjectDetails(self):
        called_func = resolve("/PutTogether/Projects/ChangeProjectDetails/").func
        self.assertEqual(called_func, ChangeProjectDetails)

    def test_InviteMembers(self):
        called_func = resolve("/PutTogether/Projects/InviteMember").func
        self.assertEqual(called_func, InviteMembers)

    def test_GetProjectMembers(self):
        called_func = resolve("/PutTogether/Projects/getMembers").func
        self.assertEqual(called_func, GetProjectMembers)





if __name__ == '__main__':
    unittest.main()
