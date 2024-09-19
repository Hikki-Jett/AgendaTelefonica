from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length = 35)
    lastName = models.CharField(max_length = 35)
    phoneNumber = models.CharField(max_length = 10)
    phoneNumberWork = models.CharField(max_length = 10)
    email = models.EmailField(default = '')
