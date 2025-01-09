import scrapy
from ..items import ClavierprojetItem

class TopachatSpider(scrapy.Spider):
    name = "topachat"
    allowed_domains = ["www.topachat.com"]
    start_urls = ["https://www.topachat.com/pages/produits_cat_est_gaming_puis_rubrique_est_wg_pccla.html"]
   
    def parse(self, response):
            claviers = response.xpath('//div[@class="product-list__product-wrapper"]')
            for clavier in claviers:
                lien = clavier.xpath('./a/@href').get()
                yield response.follow(lien, self.parse_lien)

            suivante = response.xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/main/nav/div/a[5]').get()
            if suivante is not None:
                lien = response.urljoin(suivante)
                yield scrapy.Request(lien)


    def parse_lien(self, response):
            clavier = ClavierprojetItem()
            clavier['titre'] = response.xpath('//h1[@class="ps-main__product-title"]/text()').get()
            prix_texte = response.xpath("//span[contains(@class, 'offer-price__price')]/text()").get()
            prix_texte = prix_texte.replace("\u00a0", "").strip()
            clavier['prix'] = prix_texte
            clavier['site'] = 'topachat'

            yield clavier
