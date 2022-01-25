
from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((blog_url, 'blog'), namespace='blog')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
     
