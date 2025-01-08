import scrapy


class TopachatSpider(scrapy.Spider):
    name = "topachat"
    allowed_domains = ["www.topachat.com"]
    start_urls = ["https://www.topachat.com/pages/produits_cat_est_gaming_puis_rubrique_est_wg_pccla.html"]

    def parse(self, response):
        pass
