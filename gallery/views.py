from django.shortcuts import render
from .models import Gallery, GalleryImage

# Create your views here.

def home(request):

    images = GalleryImage.objects.all()

    return render(request, 'base.html', {'images' : images})

def create_gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        gallery = Gallery.objects.create(title=title, description=description)
        
        images = request.FILES.getlist('images')
        for image in images:
            GalleryImage.objects.create(gallery=gallery, image=image)

    return render(request, 'base.html')

def admin_page(request):

    return render(request, 'admin_page.html')
