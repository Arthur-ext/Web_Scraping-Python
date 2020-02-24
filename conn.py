from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('root')
client = MongoClient('mongodb://%s:%s@localhost' % (username, password), 27017)

if __name__ == "__main__":
    print(client.server_info())