# admin.py

from django.contrib import admin
from .models import Gallery, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage

class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ['title', 'description']  # Display these fields in the admin list view
    search_fields = ['title', 'description']  # Add these fields to the admin search

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'image']  # Display these fields in the admin list view

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
