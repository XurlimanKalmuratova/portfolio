from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Projects

from django.http import HttpResponse
from django.views.generic import ListView
from .forms import LoginForm
from .forms import ProjectsForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd['username'],
                password = cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated succesfully.')
                    return HttpResponseRedirect('/')
                
                
            else:
                return HttpResponse('Disabled account')
            form.save()
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    context ={
        'form': form
    }      
    return render(request, 'login.html', context)

def registration(request):
    return render(request, 'registration.html')

def project(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project.html', context)



def project_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)



def create(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='project')
    else:
        form = ProjectsForm()
    
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='project')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    projects = Projects.objects.get(pk=pk)
    projects.delete()
    return redirect(to='project')