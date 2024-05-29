from django.contrib import admin
from .models import Gallery, GalleryImage, RequestGallery, RequestGalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1  # Number of empty forms to display

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [GalleryImageInline]

class RequestGalleryImageInline(admin.TabularInline):
    model = RequestGalleryImage
    extra = 1  # Number of empty forms to display

class RequestGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [RequestGalleryImageInline]

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(RequestGallery, RequestGalleryAdmin)
