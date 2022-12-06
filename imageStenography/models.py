from django.db import models


def rename_and_path(instance, filename):
    ext = filename.split('.')[-1]
#    og_filename = filename.split('.')[0] to get the original name.
    new_filename = "images/toBeEncrypted/%s.%s" % (instance.name, ext)
    return new_filename

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField('image', upload_to=rename_and_path, blank=True, null=True)
