from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')
def detail(request):
    return render(request, 'portfolio/detail.html')
def work(request):
    return render(request, 'portfolio/work.html')
def about(request):
    return render(request, 'portfolio/about.html')
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
