import scrapy


class LdlcSpider(scrapy.Spider):
    name = "ldlc"
    allowed_domains = ["www.ldlc.com"]
    start_urls = ["https://www.ldlc.com/informatique/peripherique-pc/clavier-gamer/c4594/"]

    def parse(self, response):
        pass
