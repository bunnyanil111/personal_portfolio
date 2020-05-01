from django.shortcuts import render,get_object_or_404
from .models import Blog
def blog(request):
	blg=Blog.objects.all()
	return render(request,'blog/details.html',{'blgs':blg})
def detail(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	return render(request, 'blog/detail.html',{'blog':blog})


# Create your views here.
