from pymongo import MongoClient

DB = 'UserCloud'  # name of our collection

DB_EXAMPLE = {"login": "Dima", "password": "1q", "mail": "",
              "files": [{"/Downloads/id": {"role": "owner", "contributors": [{"login": "role"}]}}]}


# get database object
def get_DB_object():
    client = MongoClient()
    db = client[DB]
    return db


# find user
def get_user(user_name="Dima"):
    db = get_DB_object()
    return db[DB].find_one({"login": user_name})


# insert new user in DB
def create_user():
    db = get_DB_object()
    insert_id = db[DB].insert_one(DB_EXAMPLE).inserted_id
    return insert_id


# update_collection
def update_user(user_name="Dima", new_file="file"):
    db = get_DB_object()
    update_id = db[DB].update_one({"login": user_name},
                                  {'$addToSet': {"files": new_file}})
    return update_id


# delete some element of collection
def delete_file(user_name="Dima", del_file="file"):
    db = get_DB_object()
    delete_id = db[DB].update_one({"login": user_name},
                                  {'$pull': {'files': del_file}})
    return delete_id
