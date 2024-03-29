from django.db import models

class MultiMedia(models.Model):
    title = models.CharField(max_length=250, default='')

    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

# Create your models here.