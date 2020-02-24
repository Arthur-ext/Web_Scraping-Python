class Model(object):
    def __init__(self, client):
        self._client = client
        self._db = self._client['scraping']
        self._collection = self._setCollection("main")

    def _setCollection(self, collection):
        collection = self._db[collection]
        return collection

    def create(self):pass

    def save(self, content):
        self._collection.insert_one(content)

    def delete(self):pass

    def update(self):pass

    def find(self):pass
    
    def findAll(self):pass

class Team(Model):
    def __init__(self, client):
        super().__init__(client)
        self._collection = self._setCollection('teams_standings')
        