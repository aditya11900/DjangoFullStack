from django.shortcuts import render
from .models import ProjectVariety
from django.shortcuts import get_object_or_404

# Create your views here.

def project(request):
    projects = ProjectVariety.objects.all()
    return render(request, 'project/project.html', {'projects': projects}) 

def project_detail(request, project_id):
    project = get_object_or_404(ProjectVariety, pk=project_id)
    return render(request, 'project/project_detail.html', {'project': project})