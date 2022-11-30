from django.apps import AppConfig

from CyperSecPortal.settings import MEDIA_ROOT
from decrypt_data_from_image import decrypt
from encrypt_data_in_image import encrypt_data_into_image


class ImageStenographyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imageStenography'
