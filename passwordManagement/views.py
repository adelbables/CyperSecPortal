from django import forms
from django.shortcuts import render

from . import models
from .apps.password_generator import create_password
from .apps.password_validator import validate_password


# Create your views here.
class PasswordForm(forms.ModelForm):
    class Meta:
        model = models.Password
        exclude = ['password']


class PasswordValidateForm(forms.ModelForm):
    class Meta:
        model = models.Password
        exclude = ['length', 'use_capital_letters', 'use_digits', 'use_symbols']


def generate(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            created_password = create_password(form.cleaned_data['length'], form.cleaned_data['use_capital_letters'],
                                               form.cleaned_data['use_digits'], form.cleaned_data['use_symbols'])
            return render(request, 'password_generator.html',
                          dict(password_form=form, created_password=created_password))

    else:
        form = PasswordForm()
    return render(request, 'password_generator.html', dict(password_form=form))


def validate(request):
    if request.method == "POST":
        form = PasswordValidateForm(request.POST)
        if form.is_valid():
            value = validate_password(form.cleaned_data['password'])
            return render(request, 'password_validator.html',
                          dict(password_validate_form=form, result=value))

    else:
        form = PasswordValidateForm()
    return render(request, 'password_validator.html',
                  dict(password_validate_form=form))
