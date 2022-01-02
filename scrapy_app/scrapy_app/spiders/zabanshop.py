import scrapy
from ..items import ZabanshopItem
from main_app.models import Publisher


def IdWrapper(url):
    url = url.split("/")
    book_id = url[3]
    book_id = book_id.split("-")
    book_id = book_id[1]
    return int(book_id)


def price_checker(price):
    price = price
    price = price.split("تومان")
    price = price[0].split(",")
    price = "".join(price)
    return int(price)


class ZabanshopSpider(scrapy.Spider):
    """zaban.shop, vircho sucks at api :)"""

    name = "zabanshop"
    allowed_domains = ["zaban.shop"]
    start_urls = [
        "https://www.zaban.shop/product/list/search/?pto=9999999&pageItems=2000"
    ]

    def parse(self, response):
        zabanshop = Publisher.objects.filter(id=2).first()
        for product in response.css("div.product-item"):

            item = ZabanshopItem()
        
            item["title"] = product.css("a.product-name::text").get().strip()
            item["ref"] = product.css("a.product-name::attr(href)").get().strip()
            item["status"] = True
            item["book_id"] = IdWrapper(
                product.css("a.product-name::attr(href)").get()
            )
            item["img"] = product.css("img.img-responsive::attr(src)").get()

            if product.css("span.productOldPrice::text"):
                item["current_price"] = price_checker(product.css("span.productOldPrice::text").get())
                item["special_price"] = price_checker(product.css("span.productSpecialPrice::text").get())
            elif product.css("span.productPrice::text"):
                item["current_price"] = price_checker(product.css("span.productPrice::text").get()) 
                item["special_price"] = 0 
            else:                   
                item["current_price"] = 0
                item["special_price"] = 0
                
            item["publisher"] = zabanshop
            
            yield item

        next_page = response.css(
            ".pagination-next  a:nth-child(1)::attr(href)"
        ).get()
        if next_page is not None:
            next_page = next_page + "&pageItems=2000"
            yield scrapy.Request(next_page, callback=self.parse)
