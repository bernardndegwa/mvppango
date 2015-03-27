from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

# Create your models here.
class Course(models.Model):
    title = models.TextField(default='')
    
    def __str__(self):
        return self.name
    #pass

class CourseSection(models.Model):
    title = models.TextField(default='')
    course = models.ForeignKey(Course)
    
    def __str__(self):
        return self.name

class SubSection(models.Model):
    title = models.TextField(default='')
    coursesection = models.ForeignKey(CourseSection)
    
    def __str__(self):
        return self.name    

class Question(models.Model):
    text = models.TextField(default='')
    subsection = models.ForeignKey(SubSection)
    
    def __str__(self):
        return self.name
    
class Answer(models.Model):
    text = models.TextField(default='')
    question = models.ForeignKey(Question)
    
    def __str__(self):
        return self.name