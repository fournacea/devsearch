from django.urls import path

from . import views


urlpatterns = [
    path('projects/', views.projects, name = 'projects'),
    path('project/<str:pk>/', views.project, name = 'project'),
    path('create-project/', views.create_project, name = 'create-project'),
    # path('delete-project/', views.delete_project, name = 'delete-project'),
    # path('update-project/', views.update_project, name = 'update-project'),

]
