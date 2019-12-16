from rest_framework import serializers
from .models import Stock
from products.serializers import ProductSerializer


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    #latest_price = serializers.IntegerField()

    class Meta:
        model = Stock
        fields = ('id', 'product', 'description', 'is_active',
                 'cost', 'surcharge', 'price', 'number_of_product')


class StockListSerializer(serializers.Serializer):
    product = serializers.IntegerField(read_only=True)
    number_product = serializers.IntegerField()
    base_product = ProductSerializer(read_only=True)