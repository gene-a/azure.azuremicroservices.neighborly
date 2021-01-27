import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborlycosmosdb:ZkekvJWLBSRD34JiXU4c3DlI9OnHpD5ofi9XBfaatTy6rtcVtY2R6DVaN62snl3urrJhFzoYT50YMcHT8cESww==@neighborlycosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['neighborlydb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
