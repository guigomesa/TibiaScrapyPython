# -*- coding: utf-8 -*-
import scrapy
from ..items import Mundo, AchievementsJogador, Jogador, MorteJogador, ScrapytibiaItem
import datetime

class TibiaSpider(scrapy.Spider):
    name = 'Tibia'
    allowed_domains = ['tibia.com']
    start_urls = ['https://secure.tibia.com/community/?subtopic=worlds']

    def parse(self, response):

        mundos = response.css('.TableContent a')

        for mundo in mundos:            
            urlMundo = mundo.xpath('@href').extract()
            yield scrapy.Request(url=urlMundo,callback=self.parse_mundo)
        pass

    def parse_mundo(self,response):
        mundo = Mundo()
        mundo.DataScrapy = datetime.datetime.now()
        mundo.Nome = response.css('select[name=world]').xpath('option[@selected]/text()').extract()
        mundo.Status
        pass

    def parse_jogador(self, response):

        pass