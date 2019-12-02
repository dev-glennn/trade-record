import json
import pymysql
import db as mydb
import scraping as sc

def lambda_handler():

    company=("upbit","bithumb","bittrex")
    coin=("BTC","ETH","XRP","EOS","BCH")

    for co in coin:
        result=sc.upbit(co)
        mydb.insert(result)
        result=sc.bithumb(co)
        mydb.insert(result)
        if(co!="EOS"): #bittrex API에는 EOS가 없음
            result=sc.bittrex(co)
            mydb.insert(result)

    return {
        'statusCode': 200,
        'body': "success"
    }

lambda_handler()
