from django.shortcuts import render
# from .models import Order, ProductInOrder
from django.shortcuts import render, redirect
from rest_framework.response import Response
# from .serializers import ProductInOrderSerializer
# from rest_framework import generics
# from rest_framework import viewsets


# class ProductInOrderViewSet(viewsets.ModelViewSet):
#     queryset = ProductInOrder.objects.all()
#     serializer_class = ProductInOrderSerializer