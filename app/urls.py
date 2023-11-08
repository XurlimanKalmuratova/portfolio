from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('project/', views.Project.as_view(), name='project'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),

]    