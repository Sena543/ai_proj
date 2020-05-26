from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title