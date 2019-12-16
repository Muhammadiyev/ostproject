from django.contrib import admin
from .models import Status, StockInOrder, Order


class StockInOrderInline(admin.TabularInline):
    model = StockInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class StockInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockInOrder._meta.fields]

    class Meta:
        model = StockInOrder


admin.site.register(StockInOrder, StockInOrderAdmin)

# class StockInBasketAdmin(admin.ModelAdmin):
# 	list_display = [field.name for field in StockInBasket._meta.fields]
# 	class Meta:
# 		model = StockInBasket

# admin.site.register(StockInBasket, StockInBasketAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
