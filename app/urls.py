from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('project/',project, name='project'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('create/', create, name='create'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('project/<pk>/update/', update, name='update'),
    path('project/<pk>/delete/', delete, name='delete'),

]    