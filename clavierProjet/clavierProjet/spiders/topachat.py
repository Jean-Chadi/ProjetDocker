import scrapy
from ..items import ClavierItem

class TopachatSpider(scrapy.Spider):
    name = "topachat"
    allowed_domains = ["www.topachat.com"]
    start_urls = ["https://www.topachat.com/pages/produits_cat_est_gaming_puis_rubrique_est_wg_pccla.html"]
   
    def parse(self, response):
            claviers = response.xpath('//div[@class="product-list__product-wrapper"]')
            for clavier in claviers:
                lien = clavier.xpath('./a/@href').get()
                yield response.follow(lien, self.parse_lien)

            suivante = response.xpath('//div[@class="pl-pagination"]/a[@class="pl-pagination__nav custom-link"]/@href').get()
            if suivante is not None:
                lien = response.urljoin(suivante)
                yield scrapy.Request(lien)


    def parse_lien(self, response):
            clavier = ClavierItem()
            clavier['titre'] = response.xpath('//div[@class="offer-price__start"]/span[@class="offer-price__start-tooltip-price offer-price__start-tooltip-price--sales"]/text()').get()
            clavier['prix'] = response.xpath('//div[@class="offer-price__start"]/span[@class="offer-price__start-tooltip-price offer-price__start-tooltip-price--sales"]/text()').get()
         

            yield clavier
