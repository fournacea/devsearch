from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Project
from .forms import ProjectForm


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects'))
    
    ctx = {'form': form}

    return render(request, 'projects/create-form.html', ctx)


def delete_project(request, pk):
    project = Project.objects.get(id = pk)
    
    if request.method == 'POST':
        project.delete()
        return HttpResponseRedirect(reverse('projects'))

    ctx = {'object': project}

    return render(request, 'projects/delete-template.html', ctx)


def projects(request):
    projects = Project.objects.all()

    ctx = {'projects': projects}

    return render(request, 'projects/projects.html', ctx)


def project(request, pk):
    project_obj = Project.objects.get(id = pk)

    ctx = {'project': project_obj}

    return render(request, 'projects/single-project.html', ctx)


def update_project(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects'))
    
    ctx = {'form': form, 'project': project}
 
    return render(request, 'projects/update-form.html', ctx)

