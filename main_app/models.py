from django.db import models
import datetime

# NOTE: please do `manage.py migrate`,
# and for import data to DB do `manage.py loaddata [example.json]`, please first import publisher data.\


class Product(models.Model):
    """List of our main product(Books) that other books from `Book` table
    just connect to a main product in this table"""

    class Meta:
        db_table = "Product"

    title = models.CharField(max_length=255, help_text="name of our product")
    ref = models.URLField(max_length=555, null=True)
    img = models.CharField(
        max_length=255, help_text="link of image", null=True
    )
    current_price = models.IntegerField()
    special_price = models.IntegerField()
    status = models.BooleanField(default=False)
    created_at  = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at  = models.DateTimeField(null=True, blank=True, auto_now=True)


class Publisher(models.Model):
    """list of the publishers."""

    class Meta:
        db_table = "Publisher"

    publisher_name = models.CharField(
        max_length=75, help_text="name of the publisher"
    )
    
    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    """List of other websites books :) crawl for fun fella"""

    class Meta:
        db_table = "Book"

    title = models.CharField(max_length=255, help_text="the title of the book")
    img = models.CharField(
        max_length=255, help_text="link of image", null=True
    )
    book_id = models.CharField(
        max_length=75, help_text="real book id on their own website"
    )
    current_price = models.IntegerField()
    special_price = models.IntegerField()
    ref = models.URLField(null=True, max_length=555)
    status = models.BooleanField(default=False)
    created_at  = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at  = models.DateTimeField(null=True, blank=True, auto_now=True)
    parent = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True
    )  # TODO: change on_delete=models.CASCADE later
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True
    )

class Book_Price_history(models.Model):
    """ 
        append history of book's prices.
    """
    class Meta:
        db_table = "Book_Price_history"
    
    current_price = models.IntegerField()
    special_price = models.IntegerField()
    created_at  = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    Book_id = models.ForeignKey(Book, on_delete=models.CASCADE)