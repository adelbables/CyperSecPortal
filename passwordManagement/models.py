from django.db import models


# Create your models here.

class Password(models.Model):
    password = models.CharField(max_length=200)
    length = models.IntegerField()
    use_capital_letters = models.BooleanField(default=False)
    use_digits = models.BooleanField(default=False)
    use_symbols = models.BooleanField(default=False)
