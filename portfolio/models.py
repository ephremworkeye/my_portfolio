from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE, blank=True)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=250, blank=True)
    zipcode = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='portfolio/%Y/%m/%d',blank=True)
    website = models.URLField(max_length=250)
    github = models.URLField(max_length=250, null=True)
    profession = models.CharField(max_length=100, null=True)
    education = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("portfolio:about", args=[self.id])
    

    def __str__(self):
        return self.first_name


class Portfolio(models.Model):
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, null=True)
    description = models.TextField()
    website_link = models.URLField(max_length=250, blank=True)
    github_link = models.URLField(max_length=350, blank=True)
    skill = models.ManyToManyField('Skill', through='PortfolioSkill')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("portfolio:detail", args=[self.id, self.slug])
    

    class Meta:
        ordering =('-created_at',)
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=120)
    rate = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
 
class PortfolioSkill(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE,)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.portfolio }, { self.skill }'


class Testimonial(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    body = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=250)
    message = models.TextField()