from django.shortcuts import render
from django.http import HttpResponse


project_list = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Sell things and stuff',
    },
        {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'See things I built and stuff',
    },
        {
        'id': '3',
        'title': 'social Network',
        'description': 'Chat with friends',
    }
]

def projects(request):
    msg = "Hello!"
    msg2 = "You are on the projects page"
    ctx = {'message1': msg, 'message2' : msg2, 'projects': project_list}
    return render(request, 'projects/projects.html', ctx)


def project(request, pk):
    
    project_obj = None
    for item in project_list:
        if item['id'] == pk:
            project_obj = item

    ctx = {'projects': project_list, 'project_obj': project_obj ,'hello': 'world'}

    return render(request, 'projects/single-project.html', ctx)