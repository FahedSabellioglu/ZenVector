# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import string
import random

class EmailAuthenticate(object):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self,user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None


class UserManager(BaseUserManager):
    def create_user(self,username,email,password):
        if not email:
            raise ValueError("Users must have a password")
        usr_obj = self.model(
            email = self.normalize_email(email)
        )
        usr_obj.username= email
        usr_obj.set_password(password)
        usr_obj.save(using=self._db)
        return usr_obj


class Users(AbstractUser):
    usr_name = models.CharField(max_length=255,unique=False)
    email = models.EmailField(max_length=500,primary_key=True)
    password = models.CharField(max_length=255)
    account_type = models.CharField(max_length=5)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usr_name']
    is_active = models.BooleanField(default=True)
    objects = UserManager()


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    creation_time = models.TimeField(auto_now_add=True)
    creation_date = models.DateField(auto_now_add=True)
    usr_email = models.ForeignKey(Users,db_column='email')


class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    project_id = models.ForeignKey(Projects,db_column='project_id')
    state_color = models.CharField(max_length=255,default='#59A61E')


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_deadline = models.DateField()
    task_descrip = models.TextField()
    task_state = models.ForeignKey(state,db_column='state_name')
    task_creation_time = models.TimeField(auto_now_add=True)
    task_creation_date = models.DateField(auto_now_add=True)
    task_project_id = models.ForeignKey(Projects,db_column='project_id')
    task_given_by = models.ForeignKey(Users,db_column='email')
    task_position = models.IntegerField()


class UsrProjects(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    project_id = models.ForeignKey(Projects,db_column='project_id')

class UsrTasks(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    task_id = models.ForeignKey(Tasks,db_column='task_id')


def random_pass():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(8))


class PasswordCodes(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    code = models.CharField(default=random_pass,max_length=15)
    isUsed = models.BooleanField(default=False)








