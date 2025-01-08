import scrapy
from ..items import ClavierprojetItem


class LdlcSpider(scrapy.Spider):
    name = "ldlc"
    allowed_domains = ["www.ldlc.com"]
    start_urls = ["https://www.ldlc.com/informatique/peripherique-pc/clavier-gamer/c4594/"]

    def parse(self, response):
        claviers = response.xpath("//div[@class='listing-product']/ul/li[@class='pdt-item']")
        for clavier in claviers:
            # Lien pour accéder à la page du clavier
            lien = clavier.xpath("./div[@class='dsp-cell-right']/div[@class='pdt-info']/div[@class='pdt-desc']/h3/a/@href").get()
            yield response.follow(lien, self.parse_lien)
        
        # Lien pour accéder à la page suivante et récupérer les informations de chaque pages
        suivante = response.xpath('//li[@class="next"]/a/@href').get()
        if suivante is not None:
            lien = response.urljoin(suivante)
            yield scrapy.Request(lien)


    def parse_lien(self, response):
        keyboard = ClavierprojetItem()
        keyboard['titre'] = response.xpath("//h1[@class='title-1']/text()").get()
        keyboard['prix'] = response.xpath("//div[@class='price']/div/text()").get()
        keyboard['site'] = 'topachat'

        yield keyboard
