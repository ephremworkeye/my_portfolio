from django.db import models
from django.contrib.auth.models import User


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
    photo = models.ImageField(upload_to='about/%Y/%m/%d/',blank=True)
    website = models.URLField(max_length=250)
    education = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True)
    description = models.TextField()
    profile = models.ForeignKey('Profile', related_name='profile_portfolio', on_delete=models.CASCADE)
    website_link = models.URLField(max_length=250, blank=True)
    github_link = models.URLField(max_length=350, blank=True)
    skill = models.ManyToManyField('Skill', through='PortfolioSkill')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('-created_at',)
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=120)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
 
class PortfolioSkill(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE,)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)


class Testimonial(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    