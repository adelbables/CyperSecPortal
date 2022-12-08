from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', views.register),
]
