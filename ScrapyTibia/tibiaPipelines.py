import pymongo
from scrapy.conf import settings
from .items import Mundo, Player


class TibiaMongoBasePipeline(object):

    def __init__(self):
        self._connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self._db = self._connection[settings['MONGODB_DB']]

        self._collecionWorld = self._db[settings['MONGODB_COLLECTION_WORLD']]
        self._collecionPlayer = self._db[settings['MONGODB_COLLECTION_PLAYER']]
        pass
    pass

    def process_item(self, item, spider):
        
        return item
        pass


class TibiaPlayerPipeline(TibiaMongoBasePipeline):

    def __init__(self):
        super().__init__()

    def process_item(self, item, spider):

        if not isinstance(item, Player):
            return item

        self._collecionPlayer.insert(dict(item))

        return item


class TibiaMundoPipeline(TibiaMongoBasePipeline):

    def __init__(self):
        super().__init__()

    def process_item(self, item, spider):

        if not isinstance(item, Mundo):
            return item
        
        self._collecionWorld.insert(dict(item))

        return item