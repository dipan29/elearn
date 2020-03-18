from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


from accounts.models import User
from courses.models import Course


class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolls')
    enable_access = models.BooleanField(default=False, help_text="Making this True will enable the user to access the course, after payment is recieved")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return "Enrollment --> "+self.user.first_name+"::"+self.course.title[:20]


class PageInfo(models.Model):

    about = RichTextField(help_text="Enter about Information for the Website as normal Word Doc")
    contact = RichTextField(help_text="Enter Contact like email phone address like normal page")
    services = RichTextField(help_text="Enter the range of services provided to users by Insta Worthy Academy")

    facebook_link = models.CharField(max_length=300, blank=True)
    twitter_link = models.CharField(max_length=300, blank=True)
    instagram_link = models.CharField(max_length=300, blank=True)
    youtube_link = models.CharField(max_length=300, blank=True)
    vimeo_link = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = "PageInfo"
        verbose_name_plural = "PageInfo(s)"

    def __str__(self):
        return self.name
