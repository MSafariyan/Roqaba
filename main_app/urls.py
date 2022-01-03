from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:id>", views.show_product, name="show-product"),
    path("book/<int:id>/edit", views.edit_product, name="edit-product"),
    path("book/updated", views.show_updated_books, name="show-updated-books")
]
