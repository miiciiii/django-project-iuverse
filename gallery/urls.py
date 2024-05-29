from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('create_gallery/', views.create_gallery, name='create_gallery'),
    path('request_gallery/', views.request_gallery, name='request_gallery'),
    path('approve_images/', views.approve_images, name='approve_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
