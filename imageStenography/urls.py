from django.urls import path

from imageStenography import views

urlpatterns = [
    path('upload/', views.upload, name="upload"),
]
