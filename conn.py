from pymongo import MongoClient

client = MongoClient('localhost', 27017)

if __name__ == "__main__":
    print(client.server_info())