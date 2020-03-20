from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    your_niche = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    your_biggest_struggle = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True )
    contact_number = models.CharField(max_length=200, blank=True, null=True)

    are_you_an_influencer = models.BooleanField(default=False)
    are_you_a_social_media_marketeer = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        return self.first_name

    objects = UserManager()
