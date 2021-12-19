import scrapy
from main_app.models import Publisher

from ..items import ZabanmehrItem


class ZabanmehrSpider(scrapy.Spider):
    name = "zabanmehr"
    allowed_domains = ["zabanmehrpub.com"]
    start_urls = [
        "https://zabanmehrpub.com/wp-json/wc/store/products?orderby=id&order=desc&per_page=100"
    ]

    page = 1
    def parse(self, response):
        zabanmehr = Publisher.objects.filter(
            id=6
        ).first()
        results = response.json()
        self.page += 1
        if results != []:
            for result in results:
                item = ZabanmehrItem()
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
                item["publisher"] = zabanmehr

                yield item

            next_page = f"?orderby=id&order=desc&per_page=100&page={self.page}"
            if results != "":
                yield scrapy.Request(
                    response.urljoin(next_page), callback=self.parse
                )
        else:
            return "finish"
