from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountAdmin(UserAdmin):
    list_display = (
        'phone_number', 
        'first_name', 
        'last_name', 
        'creation_date',
        'is_admin',
        'is_staff',
        'is_superuser',
        )
    search_fields = ('phone_number',)
    readonly_fields = ('creation_date', 'last_login')
    
    exclude = ('last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()
    

admin.site.register(Account, AccountAdmin)
