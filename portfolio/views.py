from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Profile, Skill

# Create your views here.
def home(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    skills = Skill.objects.all().order_by('-rate')
    profile = Profile.objects.get(id=1)
    
    return render(request, 'portfolio/home.html', {'portfolios':portfolios, 'skills': skills, 'profile': profile})

def detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    skills = portfolio.skill.all()
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio, 'skills': skills})

def work(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    return render(request, 'portfolio/work.html', {'portfolios':portfolios})

def about(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, 'portfolio/about.html', {'profile', profile})

def contact(request):
    return render(request, 'portfolio/contact.html')

def terms(request):
    return render(request, 'portfolio/terms.html')

def privacy(request):
    return render(request, 'portfolio/privacy.html')

def cookies(request):
    return render(request, 'portfolio/cookies.html')

def features(request):
    return render(request, 'portfolio/features.html')
