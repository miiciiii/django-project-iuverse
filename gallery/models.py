from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"Image for {self.gallery.title}"

class RequestGallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class RequestGalleryImage(models.Model):
    gallery = models.ForeignKey(RequestGallery, related_name='request_gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='request_gallery_images/')

    def __str__(self):
        return f"Image for {self.gallery.title}"
