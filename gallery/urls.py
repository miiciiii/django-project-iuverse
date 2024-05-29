from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_page/', views.admin_page, name='admin_page'),  
    path('create_gallery/', views.create_gallery, name='create_gallery'),
    path('request_gallery/', views.request_gallery, name = 'request_gallery'),
    path('approve_images/', views.approve_images, name='approve_images'),
]
