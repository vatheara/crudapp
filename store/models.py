from django.db import models
class Product(models.Model):
    p_id = models.CharField(max_length=20)
    p_name = models.CharField(max_length=100)
    p_qty = models.CharField(max_length=20)
    p_price = models.CharField(max_length=20)
    class Meta:
        db_table = "product"
    
