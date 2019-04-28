# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorldListScrapy(scrapy.Item):
    Name = scrapy.Field()
    NumberPlayerOnline = scrapy.Field()
    Url = scrapy.Field()
    pass


class Mundo(scrapy.Item):

    Name = scrapy.Field()
    NumberPlayersOnline = scrapy.Field()
    Location = scrapy.Field()
    PvpStyle = scrapy.Field()

    pass


class Player(scrapy.Item):

    Name = scrapy.Field()
    OlderName = scrapy.Field()
    Sex = scrapy.Field()
    Profession = scrapy.Field()
    Level = scrapy.Field()
    WorldName = scrapy.Field()
    CityResidence = scrapy.Field()
    LastLoginStr = scrapy.Field()
    Deaths = scrapy.Field()
    CityResidence = scrapy.Field()
    LastLogin = scrapy.Field()
    AccountStatus = scrapy.Field()
    House = scrapy.Field()

    pass