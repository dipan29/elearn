from django.db import models
from django.utils.timezone import now

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
