from pymongo import MongoClient
from bittrex.bittrex import *
from datetime import datetime
from time import gmtime, strftime, sleep

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

client = MongoClient()
db = client.test
my_bittrex = Bittrex(None, None, api_version=API_V1_1)  # or defaulting to v1.1 as Bittrex(None, None)
pairs = [
    "BTC-ETH",
    "BTC-LTC",
    "BTC-ADA",
    "BTC-ARK"
    ]
var = 1
while var == 1:
    for i in range(len(pairs)):
        pair = pairs[i]
        dst = my_bittrex.get_ticker(pair)
        print (dst)
        result = db[pair].insert_one(
            {
                "Ticker": dst,
                "Timestamp": time
            }
        )
        print(pair + " Succesfully added")
    print("Sleeping for 10 Seconds")
    sleep(10)
