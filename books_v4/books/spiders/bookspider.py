import scrapy
from ..items import BooksItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')
        for book in books:
            lien = book.xpath('./h3/a/@href').get()
            yield response.follow(lien, self.parse_lien)
        
        suivante = response.xpath('//li[@class="next"]/a/@href').get()
        if suivante is not None:
            lien = response.urljoin(suivante)
            yield scrapy.Request(lien)


    def parse_lien(self, response):
        livre = BooksItem()
        livre['titre'] = response.xpath('//h1/text()').get()
        livre['prix'] = response.xpath('//p[@class="price_color"]/text()').get()
        livre['genre'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()

        yield livre

        

