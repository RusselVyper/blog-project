from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Comments

def home(request):
    jobs = Blog.objects.all()
    context = {'jobs': jobs}
    return render(request, 'index.html', context)


def detail(request, blog_id):
    detailView = get_object_or_404(Blog, pk=blog_id)
    comments = Comments.objects.filter(blog=detailView)
    context = {'blog': detailView, 'comments': comments }  
    return render(request, 'detail.html', context)

@login_required(login_url='account:login')
def writeBlog(request):
    if request.method == 'POST':
        author = request.POST['blog-author']
        title = request.POST['blog-title'] 
        image = request.FILES['blog-image'] 
        description = request.POST['blog-description'] 
        Blog(author=author, title=title, images=image, description=description, period=datetime.now()).save()
        return redirect('blog:home')
    context = {}
    return render(request, 'writeblog.html', context)

@login_required(login_url='account:login')
def comments(request, blog_id):
    if request.method == 'POST':
        comment = request.POST['comment']
        Comments(comment=comment, user=request.user, blog_id=blog_id).save()
        if request.user.is_authenticated:
            return redirect("blog:detail", blog_id)



