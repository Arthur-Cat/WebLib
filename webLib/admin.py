from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin
from django.utils.html import format_html
from webLib.models import Author, Book, Product, Store, ExtUser

@admin.register(Author)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', "info"]
    change_list_template = "webLib/button.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('button', self.button)]
        return urls + my_urls

    def button(self, req):
        return redirect['..']

    def info(self, obj):
        return format_html("</br>".join(obj.info()))
    info.short_description = "Инфомация"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'page_num']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['desc', 'is_logged']

    