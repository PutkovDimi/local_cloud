from pymongo import MongoClient
from bson.objectid import ObjectId

DB = 'UserCloud'  # name of our collection

DB_EXAMPLE = {"login": "", "email": "",
              "password": "",
              "files": [{"/Downloads/id": {"role": "owner", "contributors": [{"login": "role"}]}}]}


# get database object
def get_db_object():
    client = MongoClient()
    db = client[DB]
    return db


def find_user(user_id=None, email=None):
    db = get_db_object()
    if user_id:
        print(user_id)
        return db[DB].find_one({"_id": ObjectId(user_id)})
    return db[DB].find_one({"email": email})


# insert new user in DB
def create_user(login, email, password):
    db = get_db_object()
    user_fields = DB_EXAMPLE
    user_fields.update({"login": login,
                        "email": email,
                        "password": password})
    insert_id = db[DB].insert_one(user_fields).inserted_id
    return insert_id


# update_collection
def update_user(login="Dima", new_file="file"):
    db = get_db_object()
    update_id = db[DB].update_one({"login": login},
                                  {'$addToSet': {"files": new_file}})
    return update_id


# delete some element of collection
def delete_file(login="Dima", del_file="file"):
    db = get_db_object()
    delete_id = db[DB].update_one({"login": login},
                                  {'$pull': {'files': del_file}})
    return delete_id


if __name__ == '__main__':
    print(get_db_object()[DB].find_one({"_id": ObjectId('5ad773cbfdef703d31f2bc30')})["login"])
