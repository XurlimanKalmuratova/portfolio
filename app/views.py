from django.shortcuts import render
from .models import Projects
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
        }
    return render(
        request,
        'project.html',
        context
    )
