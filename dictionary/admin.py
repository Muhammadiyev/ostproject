from django.contrib import admin
from .models import Property, Category

class PropertyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Property._meta.fields]

    class Meta:
        model = Property


admin.site.register(Property, PropertyAdmin)


admin.site.register(Category)