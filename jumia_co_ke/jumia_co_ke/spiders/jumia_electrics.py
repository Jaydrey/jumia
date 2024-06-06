import scrapy


class JumiaElectricsSpider(scrapy.Spider):
    name = "jumia_electrics"
    allowed_domains = ["jumia.co.ke"]
    start_urls = ["https://jumia.co.ke"]

    def parse(self, response):
        pass
