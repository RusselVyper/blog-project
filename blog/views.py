from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    jobs = Blog.objects.all()
    context = {'jobs': jobs}
    return render(request, 'index.html', context)


def detail(request, blog_id):
    detailView = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': detailView }  
    return render(request, 'detail.html', context) 
