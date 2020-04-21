from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

from accounts.models import User
from courses.models import Course, Category
from elearn.settings import COMPANY_NAME


class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolls')
    enable_access = models.BooleanField(default=False, help_text="Making this True will enable the user to access the course, after payment is recieved")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "Enrollments"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return "Enrollment --> "+self.user.first_name+"::"+self.course.title[:20]


class PageInfo(models.Model):
    '''
    Here goes all the meta information about the company and its details
    Basically it makes this website more like wix lol.
    '''
    title = models.CharField(max_length=300, default=COMPANY_NAME , help_text="Enter the name of your page")
    email = models.CharField(max_length=100, default="Email not set", help_text="Enter your company/support email")
    currency = models.CharField(max_length=20, default="₹")
    home_banner = RichTextField(max_length=2000, default="The flashy tagline goes here", help_text="Enter the tagline in the home banner")
    news = models.CharField(max_length=300, default="Welcome! Discover your learning track, you may contact us for great discounts",
                             help_text="All lastest news here", null=True, blank=True)
    tag_1 = RichTextField(max_length=500, default="Your homepage Tagline 1 goes here !", help_text="You fancy webpage features must go in here")
    tag_2 = RichTextField(max_length=500, default="Your homepage Tagline 2 goes here !", help_text="You fancy webpage features must go in here")
    tag_3 = RichTextField(max_length=500, default="Your homepage Tagline 3 goes here !", help_text="You fancy webpage features must go in here")
    about = RichTextField(help_text="Enter about Information for the Website as normal Word Doc")
    contact = RichTextField(help_text="Enter Contact like email phone address like normal page")
    services = RichTextField(help_text="Enter the range of services provided to users")
    tnc = RichTextField(help_text="Enter the Terms and Condition", default="tnc")
    privacy_policy = RichTextField(help_text="Enter your Privacy Policy", default="privacy")
    faqs = RichTextField(help_text="Enter some FAQs", default="faqs")

    facebook_link = models.CharField(max_length=300, blank=True)
    twitter_link = models.CharField(max_length=300, blank=True)
    instagram_link = models.CharField(max_length=300, blank=True)
    linkedin_link = models.CharField(max_length=300, blank=True)
    youtube_link = models.CharField(max_length=300, blank=True)
    vimeo_link = models.CharField(max_length=300, blank=True)

    contact_number = models.CharField(max_length=14, blank=True, help_text="Enter your contact number")
    payment_id = models.CharField(max_length=300, blank=True, help_text="Enter the payment ID in which you want to get payments")
    

    class Meta:
        verbose_name = "PageInfo"
        verbose_name_plural = "PageInfo(s)"

    def __str__(self):
        return "PageInfo"

class Testimonial(models.Model):

    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='testimonials/', help_text="This field expects an user image file, 480x360 is ideal", blank=True)
    
    def __str__(self):
        return self.title


class Discount(models.Model):

    code = models.CharField(max_length=20, help_text="Enter the unique code here e.g COURSELOVE20")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    value = models.IntegerField(default=0, help_text="Enter discount in percentage")

    def __str__(self):
        return self.code