# -*- coding: utf-8 -*-
import scrapy
from ..items import Mundo, Player
import datetime
from scrapy.loader import ItemLoader


class TibiaSpider(scrapy.Spider):
    name = 'Tibia'
    allowed_domains = ['tibia.com']
    start_urls = ['https://secure.tibia.com/community/?subtopic=worlds']

    def parse(self, response):

        resp = response.xpath("//tr[@class='Odd' or @class='Even']")

        for r in resp:

            url_mundo = r.xpath("td/a/@href").extract_first()
            if url_mundo is not None:
                url_mundo = response.urljoin(url_mundo)
                yield scrapy.Request(url=url_mundo, callback=self.parse_mundo)

        pass

    def parse_mundo(self, response):

        mundo = Mundo()

        mundo['Name'] = response.xpath("//select[@name='world']/option[@selected='selected']/text()").extract_first()
        mundo['NumberPlayersOnline'] = response.xpath("//td[contains(text(),'Players Online:')]/following-sibling::td[1]/text()").extract_first()
        mundo['Location'] = response.xpath("//td[contains(text(),'Location:')]/following-sibling::td[1]/text()").extract_first()
        mundo['PvpStyle'] = response.xpath("//td[contains(text(),'PvP Type:')]/following-sibling::td[1]/text()").extract_first()


        players = response.xpath("//tr[@class=\"Odd\" or @class=\"Even\"]/td/a/@href").extract()

        for player_url in players:

            yield scrapy.Request(url=player_url, callback=self.parse_player)

        yield mundo

        pass

    def parse_player(self, response):

        player = Player()

        player['Name'] = response.xpath("//td[@width='20%'][contains(text(),'Name:')]/following-sibling::td[1]/text()").extract_first()
        player['OlderName'] = response.xpath("//td[contains(text(),'Former Names:')]/following-sibling::td[1]/text()").extract_first()
        player['Sex'] = response.xpath("//td[contains(text(),'Sex:')]/following-sibling::td[1]/text()").extract_first()
        player['Profession'] = response.xpath("//td[contains(text(),'Vocation:')]/following-sibling::td[1]/text()").extract_first()
        player['Level'] = response.xpath("//td[contains(text(),'Level:')]/following-sibling::td[1]/text()").extract_first()
        player['WorldName'] = response.xpath("//td[contains(text(),'World:')]/following-sibling::td[1]/text()").extract_first()
        player['CityResidence'] = response.xpath("//td[contains(text(),'Residence:')]/following-sibling::td[1]/text()").extract_first()
        player['House'] = response.xpath("//td[contains(text(),'House:')]/following-sibling::td[1]/text()").extract_first()
        player['LastLogin'] = response.xpath("//td[contains(text(),'Last Login:')]/following-sibling::td[1]/text()").extract_first()
        player['AccountStatus'] = response.xpath("//table/tbody/tr/td[contains(text(),'Account')]/following-sibling::td[1]/text()").extract_first()

        yield player

        pass