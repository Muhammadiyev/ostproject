from rest_framework import serializers
from .models import Order, Status, ProductInOrder, ProductInBasket
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ProductInOrderSerializer(serializers.ModelSerializer):

    # order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductInOrder
        fields = '__all__'