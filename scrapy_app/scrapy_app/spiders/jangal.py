import scrapy

from ..items import JangalItem
from main_app.models import Publisher


class JangalSpider(scrapy.Spider):
    """jangal using json api then we just need to load json objects"""

    name = "jangal"
    allowed_domains = ["jangal.com"]
    start_urls = ["http://jangal.com/api/ui/uiproduct/list"]
    page = 1

    def parse(self, response):
        results = response.json()
        jangal = Publisher.objects.filter(id=1).first()
        self.page += 1
        total_product = results["TotalCount"]
        total_page = round(int(total_product) / 28) + 1
        for result in results["Data"]:
            item = JangalItem()
            item["title"] = result["Title"]
            item["book_id"] = result["Id"]
            item["img"] = "https://www."+self.allowed_domains[0] + result["Image"]
            item["status"] = result["IsAvailable"]
            item["ref"] = "https://"+self.allowed_domains[0]+result["Url"]
            item["current_price"] = float(result["Price"])
            item["special_price"] = float(result["SpecialPrice"])
            item["publisher"] = jangal
            yield item

        next_page = f"?page={self.page}"
        if self.page < int(total_page) + 1:
            yield scrapy.Request(
                response.urljoin(next_page), callback=self.parse
            )
