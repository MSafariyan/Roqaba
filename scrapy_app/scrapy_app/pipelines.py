# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main_app.models import Book, Publisher, Product, Book_Price_history
import datetime
# TODO: we need to add history price table
# later for each pipelines,
# is this a good idea to append same data
# to a table and also hold them uptodate
# in seperate table????, you know!!, i dont know.

# NOTE: for every pipline please remember to check their spider's name.
from django.db import models

def saveItem(item_exist,item):
    item = item
    item_exist = item_exist
    print(item_exist) 
    if item_exist:
        print("####### THIS ITEM WAS EXIST ######")
        item_exist.title = item["title"]
        item_exist.status = item["status"]
        item_exist.ref = item["ref"]
        item_exist.current_price = item["current_price"]
        item_exist.special_price = item["special_price"]
        item_exist.img = item["img"]
        item_exist.save()
        price_history_last = Book_Price_history.objects.filter(Book_id=item_exist).last()
        date_time_now =  models.DateTimeField(null=True, blank=True, auto_now_add=True)
        if date_time_now != price_history_last.created_at:   
            Price_history = Book_Price_history(
                current_price=item["current_price"],
                special_price=item["special_price"],
                Book_id=item_exist,
            )
            Price_history.save()
    else:
        print("####### New Item Found..... ######")
        new_book = Book(**item)
        new_book.save()
        Price_history = Book_Price_history(
            current_price=item["current_price"],
            special_price=item["special_price"],
            Book_id=new_book,
        )
        Price_history.save()


class KetablandPipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.name == "ketabland":
            item_exist = Product.objects.filter(title=item["title"]).first()

            if item_exist:
                print("####### THIS ITEM WAS EXIST ######")
                item_exist.title = item["title"]
                item_exist.current_price = item["current_price"]
                item_exist.special_price = item["special_price"]
                item_exist.img = item["img"]
                item_exist.save()
            else:
                new_product = Product(**item)
                new_product.save()

            return item
        return item


class JangalPipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):

        if spider.name == "jangal":
            try:
                jangal = Publisher.objects.filter(
                    id=1
                ).first()
                item_exist = (
                    Book.objects.filter(book_id=item["book_id"])
                    .filter(publisher=jangal)
                    .first()
                )
                saveItem(item_exist, item)
                return item
            except Exception as e:
                return e
        return item


class IrlanguagePipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.name == 'irlanguage':
            try:
                irlanguage = Publisher.objects.filter(
                    id=5
                ).first()
                item_exist = (
                    Book.objects.filter(book_id=item["book_id"])
                    .filter(publisher=irlanguage)
                    .first()
                )
                saveItem(item_exist, item)
                return item
            except Exception as e:
                return e
        return item


class ZabanshopPipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.name == "zabanshop":
            try:
                zabanshop = Publisher.objects.filter(
                    id=2
                ).first()
                item_exist = (
                    Book.objects.filter(book_id=item["book_id"])
                    .filter(publisher=zabanshop)
                    .first()
                )
                saveItem(item_exist, item)
                return item
            except Exception as e:
                return e
        return item


class ZabanmehrPipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.name == "zabanmehr":
            try:
                zabanmehr = Publisher.objects.filter(
                    id=6
                ).first()
                item_exist = (
                    Book.objects.filter(book_id=item["book_id"])
                    .filter(publisher=zabanmehr)
                    .first()
                )
                saveItem(item_exist, item)
                return item
            except Exception as e:
                return e
        return item


class RahnamaPipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.name == "rahnama":
            try:
                rahnama = Publisher.objects.filter(
                    id=4
                ).first()
                item_exist = (
                    Book.objects.filter(book_id=item["book_id"])
                    .filter(publisher=rahnama)
                    .first()
                )
                saveItem(item_exist, item)
                return item
            except Exception as e:
                return e
        return item