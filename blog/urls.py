from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('writeblog', views.writeBlog, name='writeblog'),
    path('comments/<int:blog_id>', views.comments, name='comments'),

]


