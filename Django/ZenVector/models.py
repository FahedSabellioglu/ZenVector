# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    usr_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500,primary_key=True)
    password = models.CharField(max_length=255)

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    creation_time = models.TimeField(auto_now_add=True)
    usr_email = models.ForeignKey(Users,db_column='email')



class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_deadline = models.TimeField(auto_now_add=True)
    task_descrip = models.TextField()
    task_status = models.CharField(max_length=25)
    task_creation_time = models.TimeField(auto_now_add=True)
    task_project_id = models.ForeignKey(Projects,db_column='project_id')
    task_given_by = models.ForeignKey(Users,db_column='email')

class UsrProjects(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    project_id = models.ForeignKey(Projects,db_column='project_id')

class UsrActivity(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    last_login = models.TimeField(auto_now_add=True)



class UsrTasks(models.Model):
    usr_email = models.ForeignKey(Users,db_column='email')
    task_id = models.ForeignKey(Tasks,db_column='task_id')







