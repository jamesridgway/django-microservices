from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=255)
    order_details = models.CharField(max_length=255)