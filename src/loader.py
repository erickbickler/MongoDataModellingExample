import pymongo
import json
import certifi


def load_env():
    with open("../secrets.json", "r") as secrets_file:
        data = json.load(secrets_file)
        return data


def get_mongo_instance():
    uri = load_env()["uri"]
    ca = certifi.where()

    return pymongo.MongoClient(uri, tlsCAFile=ca)