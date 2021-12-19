import scrapy
from ..items import KetablandItem

class KetablandSpider(scrapy.Spider):
    name = 'ketabland'
    allowed_domains = ['ketab.land']
    start_urls = ['http://ketab.land/wp-json/wc/store/products?orderby=id&order=desc&per_page=100']
    page = 1
    def parse(self, response):
        results = response.json()
        self.page += 1
        if results != []:
            for result in results:
                item = KetablandItem()
                item["title"] = result["name"]
                if type(result["images"]) == dict:
                    item["img"] = result["images"]["0"]["src"]
                else:
                    item["img"] = result["images"][0]["src"]
                item["current_price"] = float(result["prices"]["regular_price"])
                item["special_price"] = float(result["prices"]["sale_price"])
                yield item
            
            next_page = f"?orderby=id&order=desc&per_page=100&page={self.page}"
            if results != "":
                yield scrapy.Request(
                    response.urljoin(next_page), callback=self.parse
                )
