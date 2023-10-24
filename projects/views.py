from django.shortcuts import render, HttpResponseRedirect
from .models import Project
from .forms import ProjectForm


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../projects')
    
    ctx = {'form': form}

    return render(request, 'projects/project-form.html', ctx)


def projects(request):
    projects = Project.objects.all()

    ctx = {'projects': projects}

    return render(request, 'projects/projects.html', ctx)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)

    ctx = {'project': project_obj}

    return render(request, 'projects/single-project.html', ctx)

