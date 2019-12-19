from ZenVector.models import *
import unittest
from datetime import datetime

class test_Models(unittest.TestCase):

    def create_User(self):
        returned_user_ob = Users.objects.create_user("test_khaled","khaled@gmail.com", "12345678")
        return returned_user_ob

    def create_project(self):
        usrObj = self.create_User()
        returned_project_ob = Projects(project_name='test project',creation_time=datetime.now(),creation_date=datetime.today().date(),usr_email=usrObj)
        returned_project_ob.save()

        return returned_project_ob,usrObj

    def test_create_User(self):
        new_User = self.create_User()
        self.assertEqual(isinstance(new_User,Users), True)
        new_User.delete()
        self.assertEqual(len(Users.objects.filter(email='khaled@gmail.com')),0)

    def test_create_project(self):
        new_project,usrObj = self.create_project()
        self.assertEqual(isinstance(new_project, Projects) and isinstance(usrObj, Users) and new_project.creation_date == datetime.today().date(), True)



