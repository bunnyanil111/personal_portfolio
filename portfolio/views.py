from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Project
def home(request):
	projects=Project.objects.all()
	return render(request,'portfolio/index.html',{'projects':projects})

def out(request):
    return HttpResponseRedirect("https://www.linkedin.com/in/anil-reddy-43a152169/")
# Create your views here.
