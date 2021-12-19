import scrapy
from ..items import IrlanguageItem
from main_app.models import Publisher
import os

# FIXME: 500 err :| ==> fixed.


class IrlanguageSpider(scrapy.Spider):
    """
    Another rubbish store but good api.
    """

    name = "irlanguage"
    allowed_domains = ["irlanguageworld.com"]
    start_urls = [
        "https://irlanguageworld.com/wp-json/wc/store/products?orderby=id&order=desc&per_page=100"
    ]
    page = 1

    def parse(self, response):
        irlanguage = Publisher.objects.filter(
            id=5
        ).first()
        results = response.json()
        self.page += 1
        if results != []:
            for result in results:
                item = IrlanguageItem()
                item["title"] = result["name"]
                item["status"] = result["is_in_stock"]
                item["book_id"] = result["id"]
                item["ref"] = (
                    result["permalink"] if result["permalink"] else "#"
                )
                image = result["images"]
                if type(image) == dict:
                    image = list(image.values())
                item["img"] = (
                    image[0]["src"] if image else "#"
                )
                item["current_price"] = (
                    float(result["prices"]["regular_price"])
                    if result["prices"]["regular_price"]
                    else 0
                )
                item["special_price"] = (
                    float(result["prices"]["sale_price"])
                    if result["prices"]["sale_price"]
                    else 0
                )
                item["publisher"] = irlanguage
                yield item

            next_page = f"?orderby=id&order=desc&per_page=100&page={self.page}"
            if results != "":
                yield scrapy.Request(
                    response.urljoin(next_page), callback=self.parse
                )
        else:
            return "finish"
