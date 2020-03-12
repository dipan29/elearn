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
    content = RichTextField()
    outcome = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(9.99)])
    level = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video = EmbedVideoField(max_length=500, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    video = EmbedVideoField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True) 
    text = models.TextField(max_length=200) 
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text