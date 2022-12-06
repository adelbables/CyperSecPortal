import os

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from CyperSecPortal.settings import MEDIA_ROOT
from imageStenography import models
from .apps.encrypt_data_in_image import encrypt_data_into_image


# Create your views here.


class ImageForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""

    class Meta:
        model = models.Image
        exclude = []


def upload(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            extension = os.path.splitext(request.FILES['file'].name)
            encrypt_data_into_image(
                '%s/images/toBeEncrypted/%s%s' % (MEDIA_ROOT, form.cleaned_data['name'], extension[1]),
                request.POST['secret_text'])
            return HttpResponseRedirect('/upload/')  # Umleitung
    else:
        form = ImageForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))
