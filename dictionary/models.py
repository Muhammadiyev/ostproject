from django.db import models
from products.models import Product

class Property(models.Model):
    power = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=100, blank=True)
    rotation_frequency = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.power

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'



class Category(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)

    def __str__(self):
	    return "%s" %self.name
    
    class Meta:
	    verbose_name = 'Категории'
	    verbose_name_plural = 'Категории'


    # @property
    # def instruments(self):
    #     return self.instruments_of_category
