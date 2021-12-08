# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StartechItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Category = scrapy.Field()
    Price = scrapy.Field()
    Description = scrapy.Field()
    # Specs = scrapy.Field()
    Status = scrapy.Field()
    Image = scrapy.Field()
    Link = scrapy.Field()
    # pass


class TechlandItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Category = scrapy.Field()
    Price = scrapy.Field()
    Description = scrapy.Field()
    # Specs = scrapy.Field()
    Status = scrapy.Field()
    Image = scrapy.Field()
    Link = scrapy.Field()
    # pass
