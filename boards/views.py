from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list(request):
    # Fetch all projects from database
    all_projects = Project.objects.all()

    # Send those projects to an html file
    return render(request, 'boards/project_list.html', {'projects': all_projects})