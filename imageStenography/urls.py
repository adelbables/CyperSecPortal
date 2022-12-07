from django.urls import path

from imageStenography import views

urlpatterns = [
    path('upload-encrypt/', views.upload_encrypt, name="upload and encrypt"),
    path('upload-decrypt/', views.upload_decrypt, name='upload and decrypt')
]
