from django.db import models


class product(models.Model):
    images = models.ImageField(upload_to='images/', default='now')
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=40)
    price = models.CharField(max_length=10, default='1000')

class logo(models.Model):
    images = models.ImageField(upload_to='logo/', default='now')
