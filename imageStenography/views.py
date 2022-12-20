import os

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render

from CyperSecPortal.settings import MEDIA_ROOT
from imageStenography import models
from .apps.decrypt_data_from_image import decrypt
from .apps.encrypt_data_in_image import encrypt_data_into_image

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


# Create your views here.


class ImageEncryptForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""

    class Meta:
        model = models.ImageToEncrypt
        exclude = []


class ImageDecryptForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""

    class Meta:
        model = models.ImageToDecrypt
        exclude = ['name']

@login_required
async def upload_encrypt(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ImageEncryptForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            extension = os.path.splitext(request.FILES['file'].name)
            print(request.FILES['file'].name)
            await encrypt_data_into_image(
                '%s/images/toBeEncrypted/%s%s' % (MEDIA_ROOT, form.cleaned_data['name'], extension[1]),
                request.POST['secret_text'], '%s%s' %(form.cleaned_data['name'], extension[1]))
            return FileResponse(open('%s/images/encrypted/%s%s' % (MEDIA_ROOT, form.cleaned_data['name'], extension[1]), 'rb'), as_attachment=True)
    else:
        form = ImageEncryptForm()  # leeres Formular
    return render(request, 'upload_encrypt.html', dict(upload_form=form))

@login_required()
async def upload_decrypt(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ImageDecryptForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            path_to_image = '%s/images/toBeDecrypted/%s' % (MEDIA_ROOT, request.FILES['file'].name)
            print(path_to_image)
            secret = await decrypt(path_to_image)
            return render(request, 'upload_decrypt.html', dict(upload_form=form, secret=secret))
    else:
        form = ImageDecryptForm()  # leeres Formular
    return render(request, 'upload_decrypt.html', dict(upload_form=form))
