from django.contrib import admin
from contact.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id' ,'first_name', 'last_name', 'create_date'
    ordering = 'id',
    list_filter = 'create_date',
    search_fields = 'id' , 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name',