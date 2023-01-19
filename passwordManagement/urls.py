from django.urls import path

from passwordManagement import views

urlpatterns = [
    path('password_generator/', views.generate, name="generate_password"),
    path('password_validator/', views.validate, name="validate_password")
]
