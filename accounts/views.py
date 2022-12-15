from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name= first_name
        return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

