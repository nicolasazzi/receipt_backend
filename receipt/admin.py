from django.contrib import admin
from .models import Item
from .models import Receipt


admin.site.register(Item)
admin.site.register(Receipt)