from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.managers import UserManager

YEAR = [(str(r), str(r)) for r in range(datetime.now().year-5, datetime.now().year+5)]
DEPT = [(d, d) for d in ['ECE', 'EEE/EE', 'AEIE', 'CSE', 'IT', 'ME', 'CE', 'CHEM', 'BT', 'FT', 'OTHER']]

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    whatsApp_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    graduation_year_of_BTech = models.CharField(choices=YEAR, max_length=5, default=datetime.now().year+2)

    name_of_your_college = models.CharField(max_length=200, blank=True, null=True)
    your_deparment_of_study = models.CharField(choices=DEPT, max_length=5, blank=True, null=True)
    class_12_mark_in_percentage = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    average_SGPA_till_last_published_semester = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        return self.first_name

    objects = UserManager()
