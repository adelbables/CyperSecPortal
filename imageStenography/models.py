from django.db import models


def rename_and_upload_to_encrypt(instance, filename):
    ext = filename.split('.')[-1]
    #    og_filename = filename.split('.')[0] to get the original name.
    new_filename = "images/toBeEncrypted/%s.%s" % (instance.name, ext)
    return new_filename


def upload_to_decrypt(instace, filename):
    instace.name = filename
    new_filename = "images/toBeDecrypted/%s" % filename
    return new_filename


# Create your models here.
class ImageToEncrypt(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField('image', upload_to=upload_to_decrypt, blank=True, null=True)


class ImageToDecrypt(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField('image_to_decrypt', upload_to=upload_to_decrypt, blank=True, null=True)
