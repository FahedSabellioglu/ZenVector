import unittest
from django.test import Client
from ZenVector.models import *

class TestViews(unittest.TestCase):

    def test_signUp(self):
        client = Client()
        response = client.post("/PutTogether/Signup/",{"mail":"test@gmail.com","name":"test","pass":"test","acc_type":"F"})
        self.assertEqual(response.status_code,200)
        Users.objects.get(email='test@gmail.com').delete()


    def test_delete_account(self):
        client = Client()
        response_notloggedin = client.post("/PutTogether/DeleteAccount/",{"password":"test"})
        self.assertEqual(response_notloggedin.status_code,302)

        urs = Users.objects.create_user(username='test',email='test@gmail.com',password='test')
        client.login(email='test@gmail.com',password='test')
        response = client.post("/PutTogether/DeleteAccount/",{"password":"test"})
        self.assertEqual(response.status_code,200)
        urs.delete()

    def test_login(self):
        client = Client()
        response = client.post("/PutTogether/Login/",{"mail":"test@gmail.com",'password':"test"})
        self.assertEqual(response.status_code,403)

    def test_project_create(self):
        client = Client()
        urs = Users.objects.create_user(username='test',email='test@gmail.com',password='test')
        client.login(email='test@gmail.com',password='test')
        response = client.post('/PutTogether/Projects/CreateProject/',{"p_name":"TEST project",'members':['none']})
        self.assertEqual(response.status_code,200)
        urs.delete()












if __name__ == '__main__':
    unittest.main()
