from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
def index(request):
    tasks = Task.objects.all()
    return render(request, 'mainpage/index.html', {'title': 'Головна сторінка сайту', 'tasks': tasks})


def about(request):
    return render(request, 'mainpage/about.html')

def create(request):
    error = ''
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була помилковой'
    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'mainpage/create.html', context)