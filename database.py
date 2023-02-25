import pymongo
def insert_to_mongo(tweets):
    def connect_to_mongo():
        client = pymongo.MongoClient(
            "mongodb+srv://pathreeswaris:1234@pathreeswari.oidclaz.mongodb.net/?retryWrites=true&w=majority")
        db = client["Youtube_Tweets_DB"]
        tweets_collection = db["Youtube_Tweets_"]
        return tweets_collection