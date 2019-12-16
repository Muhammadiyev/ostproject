from django.shortcuts import render
from django.db.models import Sum, Count,F
from django_filters import rest_framework as filters
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import StockSerializer, StockListSerializer

from .models import Stock


class StockViewSet(viewsets.ModelViewSet):

    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['product']
    queryset = Stock.objects.all()
    def get_serializer_class(self):
        serializer_class = StockSerializer

        if self.action in ['balance']:
            serializer_class = StockListSerializer

        return serializer_class

     	def get_queryset(self):
        queryset = Stock.objects.all()

        if self.action in ['balance']:
            queryset = queryset.values('product').annotate(
                number_product=Sum('number_of_product'))
            for item in queryset:
                print(item)
            print(queryset)
        return queryset

    @action(detail=False, methods=['get'])
    def balance(self, request, pk=None):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
