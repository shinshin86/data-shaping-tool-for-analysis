# -*- coding: utf_8 -*-
import pymongo
import aggr_data

client = pymongo.MongoClient('mongodb://localhost/')
db = client.slack_data

channel_datas = db.channel_data
channels = []

for channel in channel_datas.find():
    channels.append(channel)

col = db['analysis']

for channel in channels:
    channel_name = channel['name']

    # get date_total and user_total
    date_total = aggr_data.aggr_datetime(db, channel)
    user_counts = aggr_data.aggr_usercount(db, channel)

    for post in db[channel_name].find():
        col.update({'_id':post['_id']}, post, upsert=True)
        col.update({'_id':post['_id']}, {'$set':{'channel':channel_name}}, upsert=True)
        for i in date_total:
            if post['datetime'] == i['_id']:
                col.update({'_id':post['_id']}, {'$set':{'total':i['total']}}, upsert=True)
                col.update({'_id':post['_id']}, {'$set':{'user_count':user_counts}}, upsert=True)

# create analysis_user_count
user_col = db['analysis_user_count']
for channel in db['analysis'].find():
    for i in channel['user_count']:
        user_col.update({'channel': channel['channel'],'user_id': i['_id']}, { '$set': {'count':i['total']}}, upsert=True)