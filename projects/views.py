from django.shortcuts import render
from .models import project
# Create your views here.

def home(request):
    projects = project.objects
    return render(request, 'projects/home.html', {'projects':projects})
