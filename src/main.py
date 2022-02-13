from pprint import pprint
import pymongo
import json
from loader import get_mongo_instance

db = get_mongo_instance().acm_modeling_db

def query_member_by_name():
    name = input("What name would you like to search for? ")
    print(db.members.find_one({"name": name}))

def query_arcade_wins_by_week():
    week = int(input("What week would you like to search for? "))
    result = db.arcade_scores.find_one({ "week": week })
    for object in result["scores"]:
        pprint(object)

def query_highest_arcade_score():
    week = int(input("What week would you like to search for? "))
    result = db.arcade_scores.aggregate(
        [
            {"$unwind": "$scores"},
            {"$sort": { "scores": -1}},
            {"$match": {"week": week}},
            {"$group": {
                "_id": "$week", 
                "name": {"$first": "$scores.member"}, 
                "score": {"$first": "$scores.score"}
                }
            }
        ]
    )
    for object in result:
        pprint(object)

def add_new_member():
    name = int(input("What is the name of the new member? "))
    result = db.members.insert_one({"name": name})

def add_new_arcade_score():
    week = int(input("What week is this for? "))
    name = input("What is the player's name? ")
    score = int(input("What is the player's score? "))
    result = db.arcade_scores.update_one(
        {"week": week}, 
        {"$push": {
            "scores": {
                "score": score, 
                "member": name
            }
        }}
    )
    print("Updated week's scores with new score!")

def add_new_sig_member():
    sig = input("What is the sig name? ")
    name = input("What is the member's name? ")
    result = db.special_interest_groups.update_one(
        {"name": sig},
        {"$push": {
            "members": {
                "name": name
            }
        }}
    )
    print("Updated sig with new member!")

def query_sig_members():
    sig = input("What is the sig name? ")
    result = db.special_interest_groups.find_one(
        {"name": sig}
    )
    for member in result["members"]:
        pprint(member)

if __name__=='__main__':
    print("ACM Chapter Command Line application")
    print("")
    print("What do you want to do?")
    print("\t 1. Search member by name")
    print("\t 2. Retrieve scores of weekly arcade wins")
    print("\t 3. Get highest arcade score for a particular week")
    print("\t 4. Add new member")
    print("\t 5. Add new arcade score")
    print("\t 6. Enroll a member in a SIG")
    print("\t 7. Get all members of a SIG")
    choice = int(input("Please choose one option: "))
    print("")

    if choice == 1:
        query_member_by_name()
    elif choice == 2:
        query_arcade_wins_by_week()
    elif choice == 3:
        query_highest_arcade_score()
    elif choice == 4:
        add_new_member()
    elif choice == 5:
        add_new_arcade_score()
    elif choice == 6:
        add_new_sig_member()
    elif choice == 7:
        query_sig_members()