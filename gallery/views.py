from django.shortcuts import render, redirect
from .models import Gallery, RequestGallery, GalleryImage, RequestGalleryImage

def home(request):
    galleries = Gallery.objects.prefetch_related('gallery_images').all()
    request_galleries = RequestGallery.objects.prefetch_related('request_gallery_images').all()
    context = {
        'galleries': galleries,
        'request_galleries': request_galleries,
    }
    return render(request, 'base.html', context)

def create_gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        gallery = Gallery.objects.create(title=title, description=description)
        
        images = request.FILES.getlist('images')
        for image in images:
            GalleryImage.objects.create(gallery=gallery, image=image)

        return redirect('home')

    return render(request, 'base.html')

def request_gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        gallery = RequestGallery.objects.create(title=title, description=description)
        
        images = request.FILES.getlist('images')
        for image in images:
            RequestGalleryImage.objects.create(gallery=gallery, image=image)

        return redirect('home')

    return render(request, 'base.html')

def approve_images(request):
    if request.method == 'POST':
        image_ids = request.POST.getlist('images')
        for image_id in image_ids:
            try:
                request_image = RequestGalleryImage.objects.get(id=image_id)
                gallery, created = Gallery.objects.get_or_create(
                    title=request_image.gallery.title,
                    description=request_image.gallery.description
                )
                GalleryImage.objects.create(gallery=gallery, image=request_image.image)
                request_image.delete()
            except RequestGalleryImage.DoesNotExist:
                continue

    return redirect('admin_page')

def admin_page(request):
    request_galleries = RequestGallery.objects.prefetch_related('request_gallery_images').all()
    context = {
        'request_galleries': request_galleries,
    }
    return render(request, 'admin_page.html', context)
