from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='')
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    #pass

class CourseSection(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='')
    text = models.TextField(default='')
    price = models.DecimalField(decimal_places=2, max_digits=100, default=30.00)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
                                                null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    update_defaults = models.BooleanField(default=False)
    course = models.ForeignKey(Course)
       

    
    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField(default='')
    coursesection = models.ForeignKey(CourseSection)
    
    def __str__(self):
        return self.name
    
class Answer(models.Model):
    text = models.TextField(default='')
    question = models.ForeignKey(Question)
    
    def __str__(self):
        return self.name