from django.db import models
from stock.models import Stock
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from report.models import Action


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы заказа"


class Order(models.Model):
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(
        max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s  %s" % (self.id, self.customer_name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class StockInOrder(models.Model):
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    stock = models.ForeignKey(
        Stock, blank=True, on_delete=models.CASCADE, related_name="stocks")
    nmb = models.IntegerField(default=1, blank=True)
    price_per_item = models.IntegerField(default=0, blank=True)
    total_price = models.IntegerField(default=0, blank=True)  # ЦЕНА НА КОЛВО
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % (self.stock.product.name)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        price_per_item = self.stock.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        self.stock.withdraw(self.nmb)
        super(StockInOrder, self).save(*args, **kwargs)

# def product_in_order_postsave(sender, instance, created, **kwargs):
#     order = instance.order
#     all_product_in_order = StockInOrder.objects.filter(
#         order=order, is_active=True)
#     order_total_price = 0
#     for item in all_product_in_order:
#         order_total_price += item.total_price

#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)


# post_save.connect(product_in_order_postsave, sender=StockInOrder)


# class StockInBasket(models.Model):
#     order = models.ForeignKey(
#         Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     stockinorder = models.ForeignKey(
#         StockInOrder, blank=True, default=None, on_delete=models.CASCADE)
#     price_per_item = models.DecimalField(
#         max_digits=10, decimal_places=2, default=0)
#     total_price = models.DecimalField(
#         max_digits=10, decimal_places=2, default=0)
#     is_active = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     def __str__(self):
#         return " %s" % self.order

#     class Meta:
#         verbose_name = 'Товар в корзине'
#         verbose_name_plural = 'Товары в корзине'

    # def save(self, *args, **kwargs):
    #     price_per_item = self.stockinorder.total_price
    #     self.price_per_item = price_per_item

    #     super(StockInBasket, self).save(*args, **kwargs)


# def product_in_order_postsave(sender, instance, created, **kwargs):
#     order = instance.order
#     all_product_in_order = StockInBasket.objects.filter(
#         order=order, is_active=True)
#     order_total_price = 0
#     for item in all_product_in_order:
#         order_total_price += item.total_price

#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)


# post_save.connect(product_in_order_postsave, sender=StockInBasket)
