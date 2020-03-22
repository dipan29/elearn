from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils import timezone 

from accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True, auto_created=False)
    short_description = models.TextField(blank=False, max_length=60)
    content = RichTextField(help_text="Enter the entire course outflow just like you would in a word document")
    outcome = models.CharField(max_length=200, help_text="Outcome/Achievements after successful completion of the course")
    requirements = models.CharField(max_length=200, help_text="Prequisites for enroll in the Course")
    language = models.CharField(max_length=200, help_text="Medium/Languages used in the lesson videos")
    price = models.FloatField(validators=[MinValueValidator(9.99)], help_text="Price of the course, to be entered in International Currency")
    level = models.CharField(max_length=20, help_text="Level can be, 1/2/3 or Beginner/Intermidiate/Advance")
    thumbnail = models.ImageField(upload_to='thumbnails/', help_text="This field expects an image file, 480x360 is ideal")
    video = EmbedVideoField(max_length=500, blank=True, help_text="Enter the link to the video from any streaming platform, Vimeo Preffered")
    is_published = models.BooleanField(default=True, help_text="Only set this to False, when the course is under making and you wish not to make it public")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now, help_text="Updating course regularly ensures better reach")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100, help_text="Enter the Lesson's title")
    description = RichTextField(help_text="Enter the entire lesson outflow just like you would in a word document", default="Follow the lesson")
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)], help_text="Enter video clip duration in Minutes")
    video = EmbedVideoField(max_length=500, blank=True, help_text="Vimeo Video is preffered since it ensure data protection")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title+":"+self.course.title


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True) 
    text = models.TextField(max_length=200) 
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text


class Tag(models.Model):
    """
    Multiple Category mapping for courses, many to many map
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title + " " + self.category.title
    
class Watched(models.Model):
    """
    Maps the the user to lessons watched
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson.title + " " + self.user.username