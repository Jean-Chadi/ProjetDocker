# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClavierprojetItem(scrapy.Item):
    # define the fields for your item here like:
    marque = scrapy.Field()
    titre = scrapy.Field()
    image = scrapy.Field()
    prix = scrapy.Field()
    lien = scrapy.Field()
    site = scrapy.Field()
