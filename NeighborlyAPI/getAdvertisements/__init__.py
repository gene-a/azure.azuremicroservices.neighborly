import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborlycosmosdb:ZkekvJWLBSRD34JiXU4c3DlI9OnHpD5ofi9XBfaatTy6rtcVtY2R6DVaN62snl3urrJhFzoYT50YMcHT8cESww==@neighborlycosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['neighborlydb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

