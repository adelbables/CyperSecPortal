from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from imageStenography import models


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
            return HttpResponseRedirect('/upload/')  # Umleitung
    else:
        form = ImageForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))
