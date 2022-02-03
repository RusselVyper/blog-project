
from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_url
from account import urls as account_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((blog_url, 'blog'), namespace='blog')),
    path('', include((account_url, 'account'), namespace='account')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     
     
