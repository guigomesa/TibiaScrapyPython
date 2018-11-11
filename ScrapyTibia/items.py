# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytibiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Mundo(scrapy.Item):
    Nome = scrapy.Field()
    QtdPlayersOnline = scrapy.Field()
    RecordePlayersOnline = scrapy.Field()
    TipoPvp = scrapy.Field()
    InformacaoAdicional = scrapy.Field()
    Transferenciatipo = scrapy.Field()
    Status = scrapy.Field()    
    DataScrapy = scrapy.Field()
    pass

class Jogador(scrapy.Item):
    Nome = scrapy.Field()
    NomeAntigo = scrapy.Field()
    Sexo = scrapy.Field()
    Vocacao = scrapy.Field()
    Level = scrapy.Field()
    PontosAchievement = scrapy.Field()
    CidadeResidencia = scrapy.Field()
    Casa = scrapy.Field()
    MembroGuild = scrapy.Field()
    UltimoLogin = scrapy.Field()
    StatusDaConta = scrapy.Field()
    InformacaoDaConta = scrapy.Field()
    DataCriacaoConta = scrapy.Field()
    AchievementsJogador = scrapy.Field()
    DataScrapy = scrapy.Field()
    pass

class AchievementsJogador(scrapy.Item):
    TotalEstrela = scrapy.Field()
    NomeAchievement = scrapy.Field()
    pass

class MorteJogador(scrapy.Item):
    DataMorte = scrapy.Item()
    LevelMorte = scrapy.Item()
    MotivoMorteMonstro = scrapy.Item()
    MotivoMorteJogador = scrapy.Item()
    pass