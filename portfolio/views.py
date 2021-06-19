from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Profile, Skill
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    form = ContactForm()
    portfolios = Portfolio.objects.filter(is_published=True)
    skills = Skill.objects.all().order_by('-rate')
    profile = Profile.objects.get(id=1)
    
    return render(request, 'portfolio/home.html', {'portfolios':portfolios, 'skills': skills, 'profile': profile, 'form': form})

def detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    skills = portfolio.skill.all()
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio, 'skills': skills})

def work(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    return render(request, 'portfolio/work.html', {'portfolios':portfolios})

def about(request):
    profile = Profile.objects.get(id=1)
    return render(request, 'portfolio/about.html', {'profile': profile})

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['helloworld@gmail.com'],
            )
            form.save()
            submitted=True
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'portfolio/contact.html', {'form': form, 'submitted': submitted})


def terms(request):
    return render(request, 'portfolio/terms.html')

def privacy(request):
    return render(request, 'portfolio/privacy.html')

def cookies(request):
    return render(request, 'portfolio/cookies.html')

def features(request):
    return render(request, 'portfolio/features.html')
