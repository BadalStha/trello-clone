from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('new/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),

]
