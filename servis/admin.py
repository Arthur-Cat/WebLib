from django.contrib import admin
from .models import Product, Bin, Home

admin.site.register(Bin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cost', 'isActive']
    fields = ['id', 'title']
    list_filter = ['cost']
    search_fields = ['title']


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['size', 'cost', 'adr', 'bol']
    # fields = ['id', 'title']
    # list_filter = ['cost']
    # search_fields = ['title']
#admin.site.register(Product, ProductAdmin)
