from django.contrib import admin

# Register your models here.
from .models import Profile, Portfolio, Skill, PortfolioSkill, Testimonial

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(PortfolioSkill)
class PortfolioSkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass