from datetime import datetime, timezone
from django.http import JsonResponse
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

def writeBlog(request):
    if request.method == 'POST':
        author = request.POST['blog-author']
        title = request.POST['blog-title'] 
        images = request.FILES['blog-image'] 
        description = request.POST['blog-description'] 
        Blog(author=author, title=title, images=images, description=description, period=datetime.now()).save()
        return JsonResponse({"code": 1})

    context = {}
    return render(request, 'writeblog.html', context) 
