from django.contrib import admin
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ['id','product','cost','surcharge', 'price', 'description', 'is_active', 'created', 'number_of_product']
    readonly_fields = ('price',)
    class Meta:
        model = Stock


admin.site.register(Stock, StockAdmin)



