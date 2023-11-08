from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Projects

from django.http import HttpResponse
from django.views.generic import ListView
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

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
                    return HttpResponseRedirect('project/')
                
                
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


class Project(ListView):
    template_name = 'project.html'
    model = Projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()
        return context
