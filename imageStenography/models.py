from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField('image', upload_to='images/toBeEncrypted', blank=True, null=True)
