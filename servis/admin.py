from django.contrib import admin
from .models import Product, Bin

admin.site.register(Bin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cost']
    fields = ['id', 'title']
    list_filter = ['cost']
    search_fields = ['title']

#admin.site.register(Product, ProductAdmin)
