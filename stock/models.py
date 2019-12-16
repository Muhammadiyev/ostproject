from django.db import models
from products.models import Product

class Stock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
    number_of_product = models.IntegerField(default=0)
    cost = models.IntegerField(default=0,blank=True)
    surcharge = models.IntegerField(default=0,blank=True)
    price = models.IntegerField(default=0,blank=True)
    #django aggregate, django values_list
    
    @property
    def price(self):
        get_price = self.cost * (1 + self.surcharge / 100)
        return get_price

    def withdraw(self, nmb):
        if nmb > self.number_of_product:
            raise(ValueError('Not enough number_of_product'))
        self.number_of_product -= nmb
        self.save()


    def __str__(self):
        return "%s" % (self.product.name)
   
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
