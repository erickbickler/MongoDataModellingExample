import json
from loader import get_mongo_instance

def initialize_data():
    client = get_mongo_instance()
    db = client.acm_modeling_db

    # load data from json into db
    with open("../SeedData/member_data.json", "r") as member_data_file:
        # insert member data
        member_data = json.load(member_data_file)
        member_result = db.members.insert_many(member_data)

    with open("../SeedData/weekly_arcade_data.json", "r") as arcade_data_file:    
        arcade_data = json.load(arcade_data_file)
        arcade_result = db.arcade_scores.insert_many(arcade_data)

    with open("../SeedData/sig_data.json", "r") as sig_data_file:
        sig_data = json.load(sig_data_file)
        sig_result = db.special_interest_groups.insert_many(sig_data)
                

if __name__=="__main__":
    initialize_data()