from django.db import models

class Liquidation(models.Model):
    symbol = models.CharField(max_length=10)
    side = models.CharField(max_length=10)
    order_type = models.CharField(max_length=10)
    time_in_force = models.CharField(max_length=10)
    original_quantity = models.FloatField()
    price = models.FloatField()
    average_price = models.FloatField()
    order_status = models.CharField(max_length=10)
    order_last_filled_quantity = models.FloatField()
    order_filled_accumulated_quantity = models.FloatField()
    order_trade_time = models.DateTimeField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
