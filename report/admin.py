from django.contrib import admin
from .models import Account, Action

class AccountAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Account._meta.fields]

	class Meta:
		model = Account

admin.site.register(Account, AccountAdmin)

class ActionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Action._meta.fields]

	class Meta:
		model = Action

admin.site.register(Action, ActionAdmin)