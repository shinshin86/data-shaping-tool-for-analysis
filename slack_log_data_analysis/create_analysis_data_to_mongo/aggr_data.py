# -*- coding: utf_8 -*-


# get datetime count
def aggr_datetime(db, channel):
    pipeline = [
            {"$group":{ "_id":"$datetime", "total":{"$sum":1}}},
            {"$sort":{"datetime":-1}}
    ]
    result = db[channel['name']].aggregate(pipeline)['result']
    return result


# get user count
def aggr_usercount(db, channel):
    pipeline = [
            { "$group":{ "_id":"$user", "total":{ "$sum":1}}},
            { "$sort":{ "datetime":-1 } }
    ]
    result = db[channel['name']].aggregate(pipeline)['result']
    return result
