from django.shortcuts import render, get_object_or_404, redirect
from .models import Programmer, Project
from .forms import ProgrammerForm, ProjectForm

def programmer_list(request):
    programmers = Programmer.objects.all()
    return render(request, 'portfolio/programmer_list.html', {'programmers': programmers})

def programmer_detail(request, pk):
    programmer = get_object_or_404(Programmer, pk=pk)
    projects = Project.objects.filter(programmer=programmer)
    return render(request, 'portfolio/programmer_detail.html', {'programmer': programmer, 'projects': projects})

def add_programmer(request):
    if request.method == 'POST':
        form = ProgrammerForm(request.POST)
        if form.is_valid():
            programmer = form.save(commit=False)
            programmer.user = request.user
            programmer.save()
            return redirect('programmer_detail', pk=programmer.pk)
    else:
        form = ProgrammerForm()
    return render(request, 'portfolio/add_programmer.html', {'form': form})

def add_project(request, pk):
    programmer = get_object_or_404(Programmer, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.programmer = programmer
            project.save()
            return redirect('programmer_detail', pk=pk)
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form, 'programmer': programmer})
