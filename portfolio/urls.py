from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/<slug:slug>/', views.detail, name='detail'),
    path('work', views.work, name='work'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('cookies', views.cookies, name='cookies'),
    path('features', views.features, name='features'),
]
