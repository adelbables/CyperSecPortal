from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        if user.pk is not None:
            user.save()
            login(request, user)
            messages.success(request, "your account have been successfully created")
            return redirect('/')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            render(request, 'registration/sign_up.html')

    else:
        form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})
