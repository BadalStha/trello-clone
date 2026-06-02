from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm

# Create your views here.

def project_list(request):
    # Fetch all projects from database
    all_projects = Project.objects.all()

    # Send those projects to an html file
    return render(request, 'boards/project_list.html', {'projects': all_projects})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'boards/project_create.html', {'form': form})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'boards/project_detail.html', {'project': project})