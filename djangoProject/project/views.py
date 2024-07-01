from django.shortcuts import render
from .models import ProjectVariety

# Create your views here.

def project(request):
    projects = ProjectVariety.objects.all()
    return render(request, 'project/project.html', {'projects': projects}) 
