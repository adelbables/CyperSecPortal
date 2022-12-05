from django.db import models


# Create your models here.

class Password(models.Model):
    password = models.CharField(max_length=60)
    length = models.IntegerField()
    use_capital_letters = models.BooleanField
    use_digits = models.BooleanField
    use_symbols = models.BooleanField