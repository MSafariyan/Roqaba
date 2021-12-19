# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from main_app.models import Book, Product


class JangalItem(DjangoItem):
    """Jangal Items"""

    django_model = Book


class ZabanshopItem(DjangoItem):
    """Zabanshop Items"""

    django_model = Book


class IrlanguageItem(DjangoItem):
    """
    yaya-abadi Items
    """

    django_model = Book


class ZabanmehrItem(DjangoItem):
    """Zabanmehr Items"""

    django_model = Book

class RahnamaItem(DjangoItem):
    """
    import main books
    """
    django_model = Book

class KetablandItem(DjangoItem):
    """
    import main books
    """
    django_model = Product