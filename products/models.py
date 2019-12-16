from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    category = models.ForeignKey('dictionary.Category', blank=True, null=True, related_name='product_of_category',
                                 on_delete=models.CASCADE)
    firm = models.ForeignKey('company.Firm', blank=True, null=True, related_name='product_of_firm',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='stock_images')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % (self.product.name)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
