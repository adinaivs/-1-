from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView, LogoutView


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'main/login.html'

class UserLogoutView(LogoutView):
    next_page = 'home'  # Перенаправление после выхода


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта','tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'main/task_detail.html', {'task': task})