# -*- coding: utf_8 -*-
import json
import sys
import os
import pymongo
from datetime import datetime

def execute(slack_name):
    # connet to mongodb
    client = pymongo.MongoClient('localhost', 27017)

    # create mongodb
    db = client.slack_data

    # target directory (your slack is here!)
    BASE_DIR = os.path.join(os.getcwd(), slack_name)

    # User info reads from json file
    with open(os.path.join(BASE_DIR, 'users.json'), 'r') as f:
        user_data = json.load(f)

    # If it is updated on user_data, update to latest value
    col = db["user_data"]
    for i in user_data:
        col.update({'id':i['id']}, i, upsert=True)

    users_dict = {}
    for user in user_data:
        users_dict.update({user['id']:user['name']})

    # If it is updated on channel_data, update to latest value
    col = db["channel_data"]
    with open(os.path.join(BASE_DIR, 'channels.json'), 'r') as f:
        channel_data = json.load(f)

    for i in channel_data:
        col.update({'id':i['id']}, i, upsert=True)

    # Insert all data of each channel
    # The channel to be inserted is determined by seeing channel_data' value.
    for channel in db.channel_data.find({}):
        print("Insert Channels : %", channel['name'])
        col = db[channel['name']]
        dir_name = channel['name']

        # Log data insert at each channel to DB
        print("target dir : %", os.path.join(BASE_DIR, dir_name))
        log_files = os.listdir(os.path.join(BASE_DIR, dir_name))

        for log_file in log_files:
            with open(os.path.join(BASE_DIR, dir_name, log_file)) as f:
                log_data = json.load(f)

                for i in log_data:
                    i['datetime'] = datetime.fromtimestamp(float(i['ts'])).strftime("%Y%m%d")
                    col.update({'ts':i['ts']}, i, upsert=True)

# main
args = sys.argv
execute(args[1])
