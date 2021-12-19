from django.contrib import admin

from .models import Book, Publisher, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'current_price', 'special_price', 'created_at', 'updated_at']

admin.site.register(Product, ProductAdmin)

class PublisherAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['publisher_name']


admin.site.register(Publisher, PublisherAdmin)

class BookAdmin(admin.ModelAdmin):
    model = Book
    ordering = ['publisher']
    search_fields = ['title','book_id']
    list_display = ('book_id', 'title', 'current_price', 'special_price', 'publisher_name', 'created_at', 'updated_at')
    list_filter = ['publisher__publisher_name', 'created_at', 'updated_at']
    list_per_page = 30

    def publisher_name(self, obj):
        return obj.publisher.publisher_name
    
    publisher_name.admin_order_fields = 'publisher'
    publisher_name.short_description = 'Publisher name'
    
admin.site.register(Book, BookAdmin)

